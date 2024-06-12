.. |nbsp| unicode:: 0xA0 
   :trim:
	
Linear algebra: Barkla's BLAS libraries
***************************************

The Basic Linear Algebra Subprograms (`BLAS <https://www.netlib.org/blas/>`_; see also `Wikipedia <https://en.wikipedia.org/wiki/Basic_Linear_Algebra_Subprograms>`_) specify an efficient, portable set of common vector and matrix operations, frequently used across scientific domains and in high-performance computing (HPC). Many linear algebra packages are built upon BLAS, e.g. `LAPACK <https://netlib.org/lapack/>`_ and `ScaLAPACK <https://www.netlib.org/scalapack/>`_. 

BLAS implementations are usually low-level and optimised for specific architectures (e.g. parallelism, cache optimised, special floating-point hardware, critical parts written in assembler), so a 10-fold or larger performance boost may be seen over high-level for-loop matrix calculations, i.e. code written in C or Fortran.

Barkla offers BLAS libraries in various modules. A Windows library (e.g. `OpenBLAS <https://www.openblas.net/>`_) would be needed for the HTCondor pool of teaching lab and library PCs.

.. They are the de facto standard low-level routines for linear algebra libraries; the routines have bindings for both C ("CBLAS interface") and Fortran ("BLAS interface").
.. Level 1-3 BLAS {scalar, vector and vector-vector operations, matrix-vector ; matrix-matrix operations}


Building BLAS programs on Barkla
================================

#. examine the available BLAS libraries and GCC compilers. As of 2024-04-26 we have::

    $ module avail
      ...
      libs/blas/3.6.0/gcc-5.5.0
      ...
      libs/openblas/0.2.20/gcc-5.5.0
      libs/openblas/0.3.10/gcc-11.2.0
      libs/openblas/0.3.10/gcc-7.4.0 *default*
      libs/openblas/0.3.10/gcc-9.3.0
      ...
      compilers/gcc/11.2.0
      compilers/gcc/5.5.0 *default*
      compilers/gcc/6.4.0
      compilers/gcc/7.4.0
      compilers/gcc/8.3.0
      compilers/gcc/9.3.0
      compilers/gcc/system

#. load an appropriate BLAS library *and* GCC compiler (as of 2024-04-26, Barkla uses GCC 4.8.5 if no other compiler module is loaded explicitly)::

    $ module add compilers/gcc/5.5.0
    $ module add libs/openblas/0.2.20/gcc-5.5.0

   **Take care**: GCC 5.5.0 is selected above as OpenBLAS 0.2.20 is built with this compiler. Attempting to use another GCC version will lead to mysterious errors - even for correct source code, e.g. with GCC |nbsp| 4.8.5, writing to memory allocated via ``aligned_alloc()`` generates a ``segmentation fault (core dumped)`` exception.
	
#. on building your app, link the OpenBLAS library and specify the header and library locations::

		$ gcc -lopenblas -L $OPENBLASLIB -I $OPENBLASINCLUDE <MY_FILE_NAME> -o <MY_EXECUTABLE>
		
   where the OpenBLAS [``libs/openblas/0.2.20/gcc-5.5.0``] module has set variables ``OPENBLASLIB`` and ``OPENBLASINCLUDE``::

   	$ module show libs/openblas/0.2.20/gcc-5.5.0
   	  ...
   	  setenv OPENBLASLIB /opt/gridware/depots/e2b91392/el7/pkg/libs/openblas/0.2.20/gcc-5.5.0/lib
   	  setenv OPENBLASINCLUDE /opt/gridware/depots/e2b91392/el7/pkg/libs/openblas/0.2.20/gcc-5.5.0/include

   Note: apps using math functions from C's standard library should explicitly link to this (argument ``-lm``)::

     $ gcc -lm -lopenblas -L $OPENBLASLIB -I $OPENBLASINCLUDE <MY_FILE_NAME> -o <MY_EXECUTABLE>

#. create a simple test app to test that everything is working, ``myBLASTest.c``::
	
	#include<stdio.h>
	#include<stdlib.h>
	#include<cblas.h>

	int main(void)
	{
		int numElements=3, stride=1;

		float *x= (float*)aligned_alloc(sizeof(float),numElements*sizeof(float)),
			*y= (float*)aligned_alloc(sizeof(float),numElements*sizeof(float));

		x[0]=1; x[1]=2; x[2]=3;
		y[0]=4; y[1]=5; y[2]=6;

		double dotProduct= cblas_sdot(numElements,x,stride,y,stride);
		printf("Result %f (expect 32= 4+10+18)\n",dotProduct);

		free(x);
		free(y);
		return 0;
	}
	
#. build and run on local machine::

	$ gcc -lopenblas -L $OPENBLASLIB -I $OPENBLASINCLUDE myBLASTest.c -o myBLASTest
	$ ./myBLASTest
	  Result 32.000000 (expect 32= 4+10+18)
	
#. test on Barkla compute node via the ``squeue`` scheduler with submit script ``testOpenBLAS.sh``::

	!/bin/bash -l

	#SBATCH -J My OpenBLAS test
	echo "Running on "$(hostname)" at "$(date)
	./myOpenBLASExecutable > myBLASTestOutput.txt
	echo "Finished: $HOSTNAME"
	
#. then submit job and monitor progress with::
	
	$ sbatch myOpenBLASExecutable
	$ squeue -u <MY_USERNAME>
	
	
.. include:: shared/comments.rst