import math
from hashlib import sha1
long = int
xrange = range
unicode = str

rawEstimateData = [ 11817.475, 12015.0046, 12215.3792, 12417.7504, 12623.1814, 12830.0086, 13040.0072, 13252.503, 13466.178, 13683.2738, 13902.0344, 14123.9798, 14347.394, 14573.7784, 14802.6894, 15033.6824, 15266.9134, 15502.8624, 15741.4944, 15980.7956, 16223.8916, 16468.6316, 16715.733, 16965.5726, 17217.204, 17470.666, 17727.8516, 17986.7886, 18247.6902, 18510.9632, 18775.304, 19044.7486, 19314.4408, 19587.202, 19862.2576, 20135.924, 20417.0324, 20697.9788, 20979.6112, 21265.0274, 21550.723, 21841.6906, 22132.162, 22428.1406, 22722.127, 23020.5606, 23319.7394, 23620.4014, 23925.2728, 24226.9224, 24535.581, 24845.505, 25155.9618, 25470.3828, 25785.9702, 26103.7764, 26420.4132, 26742.0186, 27062.8852, 27388.415, 27714.6024, 28042.296, 28365.4494, 28701.1526, 29031.8008, 29364.2156, 29704.497, 30037.1458, 30380.111, 30723.8168, 31059.5114, 31404.9498, 31751.6752, 32095.2686, 32444.7792, 32794.767, 33145.204, 33498.4226, 33847.6502, 34209.006, 34560.849, 34919.4838, 35274.9778, 35635.1322, 35996.3266, 36359.1394, 36722.8266, 37082.8516, 37447.7354, 37815.9606, 38191.0692, 38559.4106, 38924.8112, 39294.6726, 39663.973, 40042.261, 40416.2036, 40779.2036, 41161.6436, 41540.9014, 41921.1998, 42294.7698, 42678.5264, 43061.3464, 43432.375, 43818.432, 44198.6598, 44583.0138, 44970.4794, 45353.924, 45729.858, 46118.2224, 46511.5724, 46900.7386, 47280.6964, 47668.1472, 48055.6796, 48446.9436, 48838.7146, 49217.7296, 49613.7796, 50010.7508, 50410.0208, 50793.7886, 51190.2456, 51583.1882, 51971.0796, 52376.5338, 52763.319, 53165.5534, 53556.5594, 53948.2702, 54346.352, 54748.7914, 55138.577, 55543.4824, 55941.1748, 56333.7746, 56745.1552, 57142.7944, 57545.2236, 57935.9956, 58348.5268, 58737.5474, 59158.5962, 59542.6896, 59958.8004, 60349.3788, 60755.0212, 61147.6144, 61548.194, 61946.0696, 62348.6042, 62763.603, 63162.781, 63560.635, 63974.3482, 64366.4908, 64771.5876, 65176.7346, 65597.3916, 65995.915, 66394.0384, 66822.9396, 67203.6336, 67612.2032, 68019.0078, 68420.0388, 68821.22, 69235.8388, 69640.0724, 70055.155, 70466.357, 70863.4266, 71276.2482, 71677.0306, 72080.2006, 72493.0214, 72893.5952, 73314.5856, 73714.9852, 74125.3022, 74521.2122, 74933.6814, 75341.5904, 75743.0244, 76166.0278, 76572.1322, 76973.1028, 77381.6284, 77800.6092, 78189.328, 78607.0962, 79012.2508, 79407.8358, 79825.725, 80238.701, 80646.891, 81035.6436, 81460.0448, 81876.3884, ]

biasData = [ 11816.475, 11605.0046, 11395.3792, 11188.7504, 10984.1814, 10782.0086, 10582.0072, 10384.503, 10189.178, 9996.2738, 9806.0344, 9617.9798, 9431.394, 9248.7784, 9067.6894, 8889.6824, 8712.9134, 8538.8624, 8368.4944, 8197.7956, 8031.8916, 7866.6316, 7703.733, 7544.5726, 7386.204, 7230.666, 7077.8516, 6926.7886, 6778.6902, 6631.9632, 6487.304, 6346.7486, 6206.4408, 6070.202, 5935.2576, 5799.924, 5671.0324, 5541.9788, 5414.6112, 5290.0274, 5166.723, 5047.6906, 4929.162, 4815.1406, 4699.127, 4588.5606, 4477.7394, 4369.4014, 4264.2728, 4155.9224, 4055.581, 3955.505, 3856.9618, 3761.3828, 3666.9702, 3575.7764, 3482.4132, 3395.0186, 3305.8852, 3221.415, 3138.6024, 3056.296, 2970.4494, 2896.1526, 2816.8008, 2740.2156, 2670.497, 2594.1458, 2527.111, 2460.8168, 2387.5114, 2322.9498, 2260.6752, 2194.2686, 2133.7792, 2074.767, 2015.204, 1959.4226, 1898.6502, 1850.006, 1792.849, 1741.4838, 1687.9778, 1638.1322, 1589.3266, 1543.1394, 1496.8266, 1447.8516, 1402.7354, 1361.9606, 1327.0692, 1285.4106, 1241.8112, 1201.6726, 1161.973, 1130.261, 1094.2036, 1048.2036, 1020.6436, 990.901400000002, 961.199800000002, 924.769800000002, 899.526400000002, 872.346400000002, 834.375, 810.432000000001, 780.659800000001, 756.013800000001, 733.479399999997, 707.923999999999, 673.858, 652.222399999999, 636.572399999997, 615.738599999997, 586.696400000001, 564.147199999999, 541.679600000003, 523.943599999999, 505.714599999999, 475.729599999999, 461.779600000002, 449.750800000002, 439.020799999998, 412.7886, 400.245600000002, 383.188199999997, 362.079599999997, 357.533799999997, 334.319000000003, 327.553399999997, 308.559399999998, 291.270199999999, 279.351999999999, 271.791400000002, 252.576999999997, 247.482400000001, 236.174800000001, 218.774599999997, 220.155200000001, 208.794399999999, 201.223599999998, 182.995600000002, 185.5268, 164.547400000003, 176.5962, 150.689599999998, 157.8004, 138.378799999999, 134.021200000003, 117.614399999999, 108.194000000003, 97.0696000000025, 89.6042000000016, 95.6030000000028, 84.7810000000027, 72.635000000002, 77.3482000000004, 59.4907999999996, 55.5875999999989, 50.7346000000034, 61.3916000000027, 50.9149999999936, 39.0384000000049, 58.9395999999979, 29.633600000001, 28.2032000000036, 26.0078000000067, 17.0387999999948, 9.22000000000116, 13.8387999999977, 8.07240000000456, 14.1549999999988, 15.3570000000036, 3.42660000000615, 6.24820000000182, -2.96940000000177, -8.79940000000352, -5.97860000000219, -14.4048000000039, -3.4143999999942, -13.0148000000045, -11.6977999999945, -25.7878000000055, -22.3185999999987, -24.409599999999, -31.9756000000052, -18.9722000000038, -22.8678000000073, -30.8972000000067, -32.3715999999986, -22.3907999999938, -43.6720000000059, -35.9038, -39.7492000000057, -54.1641999999993, -45.2749999999942, -42.2989999999991, -44.1089999999967, -64.3564000000042, -49.9551999999967, -42.6116000000038, ]

def bit_length(w):
    return w.bit_length()

def bit_length_emu(w):
    return len(bin(w)) - 2 if w > 0 else 0

# Workaround for python < 2.7
if not hasattr(int, 'bit_length'):
    bit_length = bit_length_emu

def get_treshold(p):
    return 400


def estimate_bias(E, p):
    bias_vector = biasData
    nearest_neighbors = get_nearest_neighbors(E, rawEstimateData)
    return sum([float(bias_vector[i]) for i in nearest_neighbors]) / len(nearest_neighbors)


def get_nearest_neighbors(E, estimate_vector):
    distance_map = [((E - float(val)) ** 2, idx) for idx, val in enumerate(estimate_vector)]
    distance_map.sort()
    return [idx for dist, idx in distance_map[:6]]


def get_alpha(p):
    if not (4 <= p <= 16):
        raise ValueError("p=%d should be in range [4 : 16]" % p)

    if p == 4:
        return 0.673

    if p == 5:
        return 0.697

    if p == 6:
        return 0.709

    return 0.7213 / (1.0 + 1.079 / (1 << p))


def get_rho(w, max_width):
    rho = max_width - bit_length(w) + 1

    if rho <= 0:
        raise ValueError('w overflow')

    return rho


class HyperLogLog(object):
    """
    HyperLogLog cardinality counter
    """

    __slots__ = ('alpha', 'p', 'm', 'M')

    def __init__(self, error_rate):
        """
        Implementes a HyperLogLog
        error_rate = abs_err / cardinality
        """

        if not (0 < error_rate < 1):
            raise ValueError("Error_Rate must be between 0 and 1.")

        # error_rate = 1.04 / sqrt(m)
        # m = 2 ** p
        # M(1)... M(m) = 0

        p = 14
        self.alpha = get_alpha(p)
        self.p = p
        self.m = 1 << p
        self.M = [ 0 for i in range(self.m) ]

    def __getstate__(self):
        return dict([x, getattr(self, x)] for x in self.__slots__)

    def __setstate__(self, d):
        for key in d:
            setattr(self, key, d[key])

    def add(self, value):
        """
        Adds the item to the HyperLogLog
        """
        # h: D -> {0,1} ** 64
        # x = h(v)
        # j = <x_0x_1..x_{p-1}>
        # w = <x_{p}x_{p+1}..>
        # M[j] = max(M[j], rho(w))

        x = long(sha1(bytes(value.encode('utf8') if isinstance(value, unicode) else value)).hexdigest()[:16], 16)
        j = x & (self.m - 1)
        w = x >> self.p

        self.M[j] = max(self.M[j], get_rho(w, 64 - self.p))

    def update(self, *others):
        """
        Merge other counters
        """

        for item in others:
            if self.m != item.m:
                raise ValueError('Counters precisions should be equal')

        self.M = [max(*items) for items in zip(*([ item.M for item in others ] + [ self.M ]))]

    def __eq__(self, other):
        if self.m != other.m:
            raise ValueError('Counters precisions should be equal')

        return self.M == other.M

    def __ne__(self, other):
        return not self.__eq__(other)

    def __len__(self):
        return round(self.card())

    def _Ep(self):
        E = self.alpha * float(self.m ** 2) / sum(math.pow(2.0, -x) for x in self.M)
        return (E - estimate_bias(E, self.p)) if E <= 5 * self.m else E

    def card(self):
        """
        Returns the estimate of the cardinality
        """

        #count number or registers equal to 0
        V = self.M.count(0)

        if V > 0:
            H = self.m * math.log(self.m / float(V))
            return H if H <= get_treshold(self.p) else self._Ep()
        else:
            return self._Ep()

hll = HyperLogLog(0.05)

n = int(input())
for _ in range(n):
    h = input()
    hll.add(h)
print(len(hll))