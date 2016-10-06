#include <stdio.h>

// From the output, start checking from the highest

int main() {
	for (int min_ext=1; min_ext <=6; min_ext++)
		for (int a=1; a<=9; a+=1)
			for (int b=1; b<=9; b+=1) {
				int sum = min_ext + a + b;

				for (int c=1; c<=10; c+=1)
					for (int d=1; d<=9; d+=1) {
						if (c + b + d != sum)
							continue;

						for (int e=1; e<=10; e+=1)
							for (int f=1; f<=9; f+=1) {
								if (e + f + d != sum)
									continue;

								for (int g=1; g<=10; g+=1)
									for (int h=1; h<=9; h+=1) {
										if (h + g + f != sum)
											continue;

										for (int i=1; i<=10; i+=1) {
											if (i + h + a != sum)
												continue;

											if (min_ext*a*b*c*d*e*f*g*h*i == 3628800
													&& min_ext+a+b+c+d+e+f+g+h+i == 55)
												printf("%i%i%i %i%i%i %i%i%i %i%i%i %i%i%i\n",
														min_ext, a, b,
														c, b, d,
														e, d, f,
														g, f, h,
														i, h, a);
										}
									}
							}
					}
			}

	return 0;
}