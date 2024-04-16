int test_function(int a, int b, bool c){
	// this is a function
	if (c == true){
		return a + b ;
	}
	else {
		return a - b ;
	}
}

int main (){
	bool add = true ;
	char _assign1 = '=';
	char String_1 [] = " + " ;
	char String_2 [] = " - " ;
	for(int i = 0; i <= (+10 / 2); i = i + 1){
		for (int j = 0x0 ; j != (5 * -1)  ; j = j - 1){
			print(i);
			print(String_1);
			print(j);
			print(_assign1);
			print(test_function(i,j,add));
		}
	}
	add = false ;
	for (int i = 0; !(i == +5); i = i + 1) {
		for (int j = 0x0; j >= -5; j = j - 1) {
			if((i % 4) == 0 || (i % 3) == 0)
				continue;
			if(j < -4 && i > 3)
				break;
			print(i);
			print(String_2);
			print(j);
			print(_assign1);
			print(test_function(i, j, add));
		}
	}
	print("this is\" a whole string no other token like '=' or 'else' or even \\\\comment should be recogized");
	char back = '\\';
	char quote = '\'';
	int _123 = 0XABCdef1230;
}