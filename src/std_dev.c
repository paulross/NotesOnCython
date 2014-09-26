#include "math.h"

#include "std_dev.h"

double std_dev(double *arr, size_t siz) {
	double mean = 0.0;
	double sum_sq;
	double *pVal;
	double diff;
	double ret;

	pVal = arr;
	for (size_t i = 0; i < siz; ++i, ++pVal) {
		mean += *pVal;
	}
	mean /= siz;

	pVal = arr;
	sum_sq = 0.0;
	for (size_t i = 0; i < siz; ++i, ++pVal) {
		diff = *pVal - mean;
		sum_sq += diff * diff;
	}
	return sqrt(sum_sq / siz);
}
