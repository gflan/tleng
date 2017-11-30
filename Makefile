.PHONY: all tests parsertests

tests:
	mkdir -p tests
	python3 src/main.py "2+({{({C/B})}/C})" -o tests/1.svg
	python3 src/main.py "({(A/B)(A/B)}^{((A/B)(A/B)_{(A_B)})})(A_{B^{B^{B}}})" -o tests/2.svg
	python3 src/main.py "(Ax+B)ˆ{A_B}(A)_{AˆA}" -o tests/3.svg
	python3 src/main.py "{a^2_1+a^2_2+...+a^2_n}/{||(a_1,...,a_n)||}" -o tests/4.svg
	python3 src/main.py "{{A^{A^{A^{A}}}_n}/{B^{B^{B}}_m}}+A+B" -o tests/5.svg
	

parsertests:
	python3 src/ParserTest.py 