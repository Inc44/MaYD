import numpy as np


def cmp(file1, file2, shallow=False, threshold=0.9995):
	with open(file1, "rb") as f1, open(file2, "rb") as f2:
		f1_bytes = np.frombuffer(f1.read(), dtype=np.uint8)
		f2_bytes = np.frombuffer(f2.read(), dtype=np.uint8)
	if f1_bytes.shape != f2_bytes.shape:
		return False
	total_bytes = f1_bytes.size
	differing_bytes = np.sum(f1_bytes != f2_bytes)
	return 1 - differing_bytes / total_bytes >= threshold
