import numpy as np
from interface import BlackBox
import time

def mse(x, y):
    a = np.array(x, dtype=int)
    b = np.array(y, dtype=int)
    return np.mean(np.square(a - b))
def orthogonal_perturbation(delta, prev_sample, target_sample):
	# Generate perturbation
	perturb = np.random.randn(prev_sample.shape[0])
	perturb /= np.linalg.norm(perturb)
	perturb *= delta * np.linalg.norm(target_sample - prev_sample)
	# Project perturbation onto sphere around target
	diff = (target_sample - prev_sample).astype(np.float32)
	diff /= np.linalg.norm(diff)
	perturb -= np.dot(perturb, diff) * diff
	# Check overflow and underflow
	overflow = (prev_sample + perturb) - np.ones_like(prev_sample) * 255.
	perturb -= overflow * (overflow > 0)
	underflow = np.zeros_like(prev_sample) - (prev_sample + perturb)
	perturb += underflow * (underflow > 0)
	return perturb

def forward_perturbation(epsilon, prev_sample, target_sample):
	perturb = (target_sample - prev_sample).astype(np.float32)
	perturb /= np.linalg.norm(target_sample - prev_sample)
	perturb *= epsilon
	return perturb

def get_diff(sample_1, sample_2):
	return np.mean((sample_1 - sample_2).astype(np.float32) ** 2)

def initial_adversarial(precision=0.5):
    bb = BlackBox()
    x = bb.get_image()
    #x = np.ones(3072) * 127
    found = False
    while not found:
        for pixel in range(x.shape[0]):
            x_mod = np.array(x)
            if x[pixel] != 0:
                x_mod[pixel] = x[pixel] - 1
            score_minus = bb.calc(x_mod)
            if x[pixel] != 255:
                x_mod[pixel] = x[pixel] + 1
            score_plus = bb.calc(x_mod)
            if score_plus > score_minus and x[pixel] != 255:
                x[pixel] += 1
                if score_plus > precision:
                    found = True
                    break
            elif score_plus < score_minus and x[pixel] != 0:
                x[pixel] -= 1
                if score_minus > precision:
                    found = True
                    break
    return x

def my_random_perturb(x):
    r = np.random.randint(0,3,size=x.shape[0]) - 1
    return r

def boundary_attack(_adversarial_sample, _target_sample):
	_delta = 0.01
	_epsilon = 0.05
	_score = 0.
	for index in range(10000):
		_epsilon = np.linalg.norm((_adversarial_sample - _target_sample).astype(np.float32))
		print(BlackBox().calc(_adversarial_sample), mse(_adversarial_sample, _target_sample), _delta, _epsilon)
		while True:
			trial_sample = _adversarial_sample + forward_perturbation(_epsilon, _adversarial_sample, _target_sample)
			prediction = BlackBox().calc(trial_sample)
			if prediction > 0.5:
				_adversarial_sample = trial_sample
				break
			else:
				_epsilon *= 0.9
		print("step1",mse(_adversarial_sample, _target_sample))
		while True:
			trial_samples = []
			for i in np.arange(10):
				trial_sample = _adversarial_sample + orthogonal_perturbation(_delta, _adversarial_sample, _target_sample)
				trial_samples.append(trial_sample)
			predictions = np.array([BlackBox().calc(smple) for smple in trial_samples])
			d_score = np.mean(predictions > 0.5)
			if d_score > 0.0:
				if d_score < 0.3:
					_delta *= 0.9
				elif d_score > 0.6:
					_delta /= 0.9
				_adversarial_sample = np.array(trial_samples)[np.where(predictions > 0.5)[0][0]]
				break
			else:
				_delta *= 0.9
		print("step2",mse(_adversarial_sample, _target_sample))
		_epsilon = np.linalg.norm((_adversarial_sample - _target_sample).astype(np.float32))
		while True:
			trial_sample = _adversarial_sample + forward_perturbation(_epsilon, _adversarial_sample, _target_sample)
			prediction = BlackBox().calc(trial_sample)
			if prediction > 0.5:
				_adversarial_sample = trial_sample
				break
			else:
				_epsilon *= 0.9


	return _adversarial_sample

start_time = time.time()
img = BlackBox().get_image().astype(np.float32)

#adv = initial_adversarial(0.5).astype(np.float32)
#np.save("task_Q.data", adv)
adv = np.load("task_Q.data.npy").astype(np.float32)


print(orthogonal_perturbation(0.05, adv, img))
print("MSE:", mse(img, adv))
old_score = mse(adv, img)

final_image = boundary_attack(adv, img)

print("Final MSE:",mse(final_image, img))
end_time = time.time()
print("time:", end_time - start_time)

#print(*final_image)