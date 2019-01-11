from led_colors import *

# Global and constant dictionary containing the letter widths of each letter.
# Letters include one space after them for margins. Sprites do not.
LETTER_WIDTHS = {
	"A" : 4,
	"B" : 4,
	"C" : 4,
	"D" : 4,
	"E" : 4,
	"F" : 4,
	"G" : 5,
	"H" : 4,
	"I" : 4,
	"J" : 4,
	"K" : 4,
	"L" : 4,
	"M" : 6,
	"N" : 6,
	"O" : 4,
	"P" : 4,
	"Q" : 6,
	"R" : 4,
	"S" : 4,
	"T" : 4,
	"U" : 4,
	"V" : 4,
	"W" : 6,
	"X" : 4,
	"Y" : 4,
	"Z" : 6,
	" " : 4,
	"!" : 2,
	"." : 2,
	"0" : 4,
	"1" : 4,
	"2" : 4,
	"3" : 4,
	"4" : 4,
	"5" : 4,
	"6" : 4,
	"7" : 4,
	"8" : 4,
	"9" : 4,
}

# Assumes that the height is 7 and width of each letter is 5. Adds the word to the matrix at start.
def draw_R(start, color, front):
	for row in range(2, 9):
		front[row][start] = color

	front[2][start + 1] = color
	front[5][start + 1] = color

	front[2][start + 2] = color
	front[3][start + 2] = color
	front[4][start + 2] = color

	front[6][start + 2] = color
	front[7][start + 2] = color
	front[8][start + 2] = color

def draw_U(start, color, front):
	for row in range(2, 9):
		front[row][start] = color
		front[row][start + 2] = color

	front[8][start + 1] = color

def draw_S(start, color, front):
	for row in range(2, 6):
		front[row][start] = color
	front[8][start] = color

	front[2][start + 1] = color
	front[5][start + 1] = color
	front[8][start + 1] = color

	for row in range(5, 9):
		front[row][start + 2] = color
	front[2][start + 2] = color

def draw_H(start, color, front):
	for row in range(2, 9):
		front[row][start] = color
		front[row][start + 2] = color

	front[5][start + 1] = color

def draw_A(start, color, front):
	for row in range(2, 9):
		front[row][start] = color
		front[row][start + 2] = color

	front[2][start + 1] = color
	front[5][start + 1] = color

def draw_B(start, color, front):
	for row in range(2,9):
		front[row][start] = color

	front[2][start + 1] = color
	front[5][start + 1] = color
	front[8][start + 1] = color

	front[2][start + 2] = color
	front[3][start + 2] = color
	front[4][start + 2] = color
	front[6][start + 2] = color
	front[7][start + 2] = color
	front[8][start + 2] = color

def draw_D(start, color, front):
	for row in range(2,9):
		front[row][start] = color

	front[2][start + 1] = color
	front[8][start + 1] = color

	for row in range(3,8):
		front[row][start + 2] = color

def draw_F(start, color, front):
	for row in range(2,9):
		front[row][start] = color

	for num in range(1,3):
		front[2][start + num] = color
		front[5][start + num] = color

def draw_I(start, color, front):
	for row in range(3,8):
		front[row][start + 1] = color
	for num in range(0, 3):
		front[2][start + num] = color
		front[8][start + num] = color

def draw_K(start, color, front):
	for row in range(2,9):
		front[row][start] = color
	front[5][start + 1] = color

	for row in range(2, 5):
		front[row][start + 2] = color

	for row in range(6, 9):
		front[row][start + 2] = color

def draw_M(start, color, front):
	for row in range(2,9):
		front[row][start] = color
		front[row][start + 4] = color
	front[3][start + 1] = color
	front[4][start + 2] = color
	front[3][start + 3] = color

def draw_O(start, color, front):
	for row in range(2,9):
		front[row][start] = color
		front[row][start + 2] = color

	front[2][start + 1] = color
	front[8][start + 1] = color

def draw_V(start, color, front):
	for row in range(2,8):
		front[row][start] = color
		front[row][start + 2] = color

	front[8][start + 1] = color

def draw_Z(start, color, front):
	for num in range(0,5):
		front[2][start + num] = color
		front[8][start + num] = color
	front[3][start + 4] = color
	front[4][start + 3] = color
	front[5][start + 2] = color
	front[6][start + 1] = color
	front[7][start] = color


def draw_C(start, color, front):
	for row in range(2, 9):
		front[row][start] = color

	for col in range(start + 1, start + 3):
		front[2][col] = color
		front[8][col] = color

def draw_E(start, color, front):
	for row in range(2, 9):
		front[row][start] = color

	for col in range(start + 1, start + 3):
		front[2][col] = color
		front[5][col] = color
		front[8][col] = color

def draw_epsilon(start, color, front):
	for row in range(2, 9):
		front[row][start + 1] = color

	for col in range(start + 2, start + 6):
		front[2][col] = color
		front[8][col] = color

	for col in range(start + 2, start + 5):
		front[5][col] = color

	front[3][start + 5] = color
	front[7][start + 5] = color

def draw_G(start, color, front):
	for row in range(2, 9):
		front[row][start] = color

	front[2][start + 1] = color
	front[8][start + 1] = color

	front[2][start + 2] = color
	front[5][start + 2] = color
	front[8][start + 2] = color

	front[2][start + 3] = color

	for row in range(5, 9):
		front[row][start + 3] = color

def draw_Y(start,color, front):
	for row in range(2, 5):
		front[row][start] = color
		front[row][start + 2] = color

	for row in range(5, 9):
		front[row][start + 1] = color


def draw_W(start,color, front):
	for row in range(2, 9):
		front[row][start] = color
		front[row][start + 4] = color

	front[6][start + 1] = color
	front[6][start + 3] = color
	front[5][start + 2] = color

def draw_T(start, color, front):
	for row in range(2, 9):
		front[row][start + 1] = color

	front[2][start] = color
	front[2][start + 2] = color

def draw_P(start, color, front):
	for row in range(2, 9):
		front[row][start] = color

	for col in range(start + 1, start + 3):
		front[2][col] = color
		front[5][col] = color

	for row in range(3, 5):
		front[row][start + 2] = color

def draw_N(start, color, front):
	for row in range(2, 9):
		front[row][start] = color
		front[row][start + 4] = color

	front[4][start + 1] = color
	front[5][start + 2] = color
	front[6][start + 3] = color

def draw_L(start, color, front):
	for row in range(2, 9):
		front[row][start] = color

	for col in range(start + 1, start + 3):
		front[8][col] = color

def draw_X(start, color, front):
	for row in range(2, 5):
		front[row][start] = color
		front[row][start + 2] = color

	for row in range(6, 9):
		front[row][start] = color
		front[row][start + 2] = color

	front[5][start + 1] = color

def draw_Q(start, color, front):
	for row in range(3, 8):
		front[row][start] = color

	for col in range(start + 1, start + 4):
		front[2][col] = color

	for row in range(3, 7):
		front[row][start + 4] = color

	front[8][start + 1] = color
	front[8][start + 2] = color
	front[6][start + 2] = color
	front[7][start + 3] = color
	front[8][start + 4] = color

def draw_J(start, color, front):
	for col in range(start, start + 3):
		front[2][col] = color

	for row in range(3, 9):
		front[row][start + 2] = color

	front[8][start + 1] = color
	front[7][start] = color

def draw_exclamation(start, color, front):
	for row in range(2, 7):
		front[row][start] = color
	front[8][start] = color

def draw_period(start, color, front):
	front[8][start] = color

def draw_zero(start, color, front):
	for row in range(3, 8):
		 front[row][start] = color
		 front[row][start + 2] = color

	front[2][start + 1] = color
	front[8][start + 1] = color

def draw_bin_zero(start, color, front):
	draw_zero(start, LIGHT_GREEN, front)

def draw_one(start, color, front):
	front[3][start] = color
	for row in range(2, 8):
		front[row][start + 1] = color

	for col in range(start, start + 3):
		front[8][col] = color

def draw_bin_one(start, color, front):
	draw_one(start, LIGHT_GREEN, front)

def draw_two(start, color, front):
	for row in range(2, 6):
		front[row][start + 2] = color
	front[8][start + 2] = color

	front[2][start + 1] = color
	front[5][start + 1] = color
	front[8][start + 1] = color

	front[2][start] = color

	for row in range(6, 9):
		front[row][start] = color

def draw_three(start, color, front):
	for row in range(2, 9):
		front[row][start + 2] = color

	for col in range(start, start + 2):
		front[2][col] = color
		front[5][col] = color
		front[8][col] = color

def draw_four(start, color, front):
	for row in range(2, 6):
		front[row][start] = color

	for row in range(2, 9):
		front[row][start + 2] = color

	front[5][start + 1] = color

def draw_five(start, color, front):
	for col in range(start, start + 3):
		front[2][col] = color

	for row in range(3, 6):
		front[row][start] = color

	front[5][start + 1] = color
	front[5][start + 2] = color

	front[8][start + 1] = color

	front[7][start] = color

	for row in range(5, 8):
		front[row][start + 2] = color

def draw_six(start, color, front):
	for col in range(start, start + 3):
		front[2][col] = color
		front[5][col] = color
		front[8][col] = color

	for row in range(2, 8):
		front[row][start] = color

	for row in range(6, 8):
		front[row][start + 2] = color

def draw_seven(start, color, front):
	for col in range(start, start + 3):
		front[2][col] = color

	front[3][start + 2] = color
	front[4][start + 2] = color

	front[5][start + 1] = color

	for row in range(6, 9):
		front[row][start] = color

def draw_eight(start, color, front):
	front[2][start + 1] = color
	front[5][start + 1] = color
	front[8][start + 1] = color

	for row in range(2, 9):
		front[row][start] = color
		front[row][start + 2] = color

def draw_nine(start, color, front):
	for col in range(start, start + 3):
		front[2][col] = color
		front[5][col] = color
		front[8][col] = color

	for row in range(2, 6):
		front[row][start] = color

	for row in range(2, 8):
		front[row][start + 2] = color

def draw_theta(start, color, front):
	# column 1
	ar = [2,6]
	for row in range(3, 8):
		for i in range(len(ar)):
			front[row][start + ar[i]] = color

	ar_row = [2,5,8]
	# column 3 to 4
	for i in range(len(ar_row)):
		for col in range(3,6):
			front[ar_row[i]][start + col] = color


def draw_tau(start, color, front):
	for col in range(2,7):
		front[2][start + col] = color
	for row in range(3,9):
		front[row][start + 4] = color
	# serif details
	front[3][start + 2] = color
	front[3][start + 6] = color

	front[8][start + 3] = color
	front[8][start + 5] = color

def draw_delta(start, color, front):
	for col in range(start, start + 7):
		front[8][col] = color

	front[7][start] = color
	front[7][start + 6] = color

	front[6][start + 1] = color
	front[5][start + 1] = color
	front[6][start + 5] = color
	front[5][start + 5] = color

	front[3][start + 2] = color
	front[4][start + 2] = color
	front[3][start + 4] = color
	front[4][start + 4] = color

	front[2][start + 3] = color


def draw_rose_left(start, color, front):
	front[3][start + 2] = DARK_RED
	front[4][start + 2] = DARK_RED

	front[2][start + 3] = LIGHT_RED
	front[3][start + 3] = DARK_RED
	front[4][start + 3] = DARK_RED
	front[5][start + 3] = DARK_RED

	front[2][start + 4] = LIGHT_RED
	front[3][start + 4] = LIGHT_RED
	front[4][start + 4] = DARK_RED
	front[5][start + 4] = DARK_RED

	front[3][start + 5] = LIGHT_RED
	front[4][start + 5] = DARK_RED
	front[5][start + 5] = DARK_GREEN
	front[7][start + 5] = LIGHT_GREEN
	front[8][start + 5] = LIGHT_GREEN

	front[6][start + 6] = DARK_GREEN
	front[7][start + 6] = LIGHT_GREEN
	front[8][start + 6] = DARK_GREEN

def draw_reverse_rose_right(start, color, front):
	front[3][start + 4] = DARK_RED
	front[4][start + 4] = DARK_RED

	front[2][start + 3] = LIGHT_RED
	front[3][start + 3] = DARK_RED
	front[4][start + 3] = DARK_RED
	front[5][start + 3] = DARK_RED

	front[2][start + 2] = LIGHT_RED
	front[3][start + 2] = LIGHT_RED
	front[4][start + 2] = DARK_RED
	front[5][start + 2] = DARK_RED

	front[3][start + 1] = LIGHT_RED
	front[4][start + 1] = DARK_RED
	front[5][start + 1] = DARK_GREEN
	front[7][start + 1] = LIGHT_GREEN
	front[8][start + 1] = LIGHT_GREEN

	front[6][start] = DARK_GREEN
	front[7][start] = LIGHT_GREEN
	front[8][start] = DARK_GREEN

def draw_rose_right(start, color, front):
	front[4][start] = LIGHT_GREEN
	front[5][start] = LIGHT_GREEN
	front[6][start] = LIGHT_GREEN

	front[4][start + 1] = LIGHT_GREEN
	front[5][start + 1] = DARK_GREEN
	front[7][start + 1] = DARK_GREEN

	front[7][start + 2] = DARK_GREEN

	front[8][start + 3] = DARK_GREEN

	front[8][start + 4] = DARK_GREEN

def draw_reverse_rose_left(start, color, front):
	front[8][start + 2] = DARK_GREEN

	front[8][start + 3] = DARK_GREEN

	front[7][start + 4] = DARK_GREEN

	front[4][start + 5] = LIGHT_GREEN
	front[5][start + 5] = DARK_GREEN
	front[7][start + 5] = DARK_GREEN

	front[4][start + 6] = LIGHT_GREEN
	front[5][start + 6] = LIGHT_GREEN
	front[6][start + 6] = LIGHT_GREEN

def draw_ht_left(start, color, front):
	front[2][start + 3] = DARK_PURPLE
	front[3][start + 3] = DARK_PURPLE

	front[2][start + 4] = DARK_PURPLE
	front[4][start + 4] = DARK_PURPLE
	front[8][start + 4] = DARK_PURPLE

	front[3][start + 5] = DARK_PURPLE
	front[4][start + 5] = DARK_PURPLE
	front[8][start + 5] = DARK_PURPLE

	front[4][start + 6] = DARK_PURPLE
	front[7][start + 6] = DARK_PURPLE

def draw_ht_mid(start, color, front):
	front[5][start] = DARK_PURPLE
	front[7][start] = DARK_PURPLE
	front[5][start + 6] = DARK_PURPLE
	front[7][start + 6] = DARK_PURPLE

	for row in range(3, 6):
		for col in range(start + 1, start + 6):
			front[row][col] = LIGHT_TAN


	for row in range(6, 8):
		for col in range(start + 1, start + 6):
			front[row][col] = DARK_TAN

	front[6][start + 4] = LIGHT_TAN
	front[6][start + 5] = LIGHT_TAN

	for col in range(col + 2, col + 5):
		front[8][col] = DARK_TAN

def draw_ht_right(start, color, front):
	front[2][start] = DARK_PURPLE
	front[4][start] = DARK_PURPLE
	front[7][start] = DARK_PURPLE

	front[2][start + 1] = DARK_PURPLE
	front[3][start + 1] = DARK_PURPLE
	front[4][start + 1] = DARK_PURPLE
	front[8][start + 1] = DARK_PURPLE

	for row in range(2, 6):
		front[row][start + 2] = DARK_PURPLE
	front[8][start + 1] = DARK_PURPLE

	for row in range(3, 6):
		front[row][start + 3] = DARK_PURPLE

def draw_plant_left(start, color, front):
	front[3][start + 5] = LIGHT_GREEN
	front[3][start + 6] = LIGHT_GREEN
	front[4][start + 4] = LIGHT_GREEN
	front[7][start + 5] = ORANGE
	front[7][start + 6] = ORANGE
	front[8][start + 4] = ORANGE
	front[8][start + 5] = ORANGE
	front[8][start + 6] = ORANGE

def draw_plant_right(start, color, front):
	front[3][start + 1] = LIGHT_GREEN
	front[3][start + 2] = LIGHT_GREEN
	front[4][start] = LIGHT_GREEN
	front[4][start + 3] = LIGHT_GREEN
	front[5][start] = LIGHT_GREEN
	front[6][start] = LIGHT_GREEN
	front[7][start] = ORANGE
	front[7][start + 1] = ORANGE
	front[7][start + 2] = ORANGE
	front[8][start] = ORANGE
	front[8][start + 1] = ORANGE
	front[8][start + 2] = ORANGE
	front[8][start + 3] = ORANGE

def draw_dna_left(start, color, front):
	front[2][start + 2] = LIGHT_BLUE
	front[2][start + 3] = LIGHT_BLUE
	front[3][start + 2] = YELLOW
	front[3][start + 4] = LIGHT_BLUE
	front[3][start + 5] = LIGHT_BLUE
	front[4][start + 2] = YELLOW
	front[4][start + 4] = YELLOW
	front[4][start + 6] = LIGHT_BLUE
	front[5][start + 2] = YELLOW
	front[5][start + 4] = YELLOW
	front[5][start + 6] = LIGHT_PURPLE
	front[6][start + 2] = YELLOW
	front[6][start + 4] = LIGHT_PURPLE
	front[6][start + 5] = LIGHT_PURPLE
	front[7][start + 2] = LIGHT_PURPLE
	front[7][start + 3] = LIGHT_PURPLE

def draw_dna_right(start, color, front):
	front[2][start + 3] = LIGHT_PURPLE
	front[2][start + 4] = LIGHT_PURPLE
	front[3][start + 1] = LIGHT_PURPLE
	front[3][start + 2] = LIGHT_PURPLE
	front[3][start + 4] = YELLOW
	front[4][start] = LIGHT_PURPLE
	front[4][start + 2] = YELLOW
	front[4][start + 4] = YELLOW
	front[5][start] = LIGHT_BLUE
	front[5][start + 2] = YELLOW
	front[5][start + 4] = YELLOW
	front[6][start + 1] = LIGHT_BLUE
	front[6][start + 2] = LIGHT_BLUE
	front[6][start + 4] = YELLOW
	front[7][start + 3] = LIGHT_BLUE
	front[7][start + 4] = LIGHT_BLUE

def draw_build_left(start, color, front):
	for col in range(start + 2, start + 7):
		front[3][col] = DARK_PURPLE
		front[5][col] = DARK_PURPLE
		front[7][col] = DARK_PURPLE
	front[4][start + 2] = DARK_PURPLE
	front[4][start + 4] = DARK_PURPLE
	front[4][start + 6] = DARK_PURPLE
	front[6][start + 2] = DARK_PURPLE
	front[6][start + 4] = DARK_PURPLE
	front[6][start + 6] = DARK_PURPLE
	front[8][start + 2] = DARK_PURPLE
	front[8][start + 4] = DARK_PURPLE
	front[8][start + 6] = DARK_PURPLE
	front[4][start + 3] = YELLOW
	front[4][start + 5] = YELLOW
	front[6][start + 3] = YELLOW
	front[6][start + 5] = YELLOW
	front[8][start + 3] = YELLOW
	front[8][start + 5] = YELLOW

def draw_build_right(start, color, front):
	front[5][start + 1] = DARK_PURPLE
	front[5][start + 3] = DARK_PURPLE
	for col in range(start, start + 5):
		front[6][col] = DARK_PURPLE
		front[7][col] = DARK_PURPLE
	front[8][start] = DARK_PURPLE
	front[8][start + 4] = DARK_PURPLE
	front[8][start + 1] = YELLOW
	front[8][start + 2] = YELLOW
	front[8][start + 3] = YELLOW

def draw_potion(start, color, front):
	front[2][start + 5] = LIGHT_BLUE
	front[2][start + 6] = LIGHT_BLUE
	front[3][start + 6] = LIGHT_BLUE
	front[4][start + 6] = LIGHT_BLUE
	front[5][start + 5] = LIGHT_BLUE
	front[5][start + 6] = WHITE
	front[6][start + 4] = LIGHT_BLUE
	front[6][start + 5] = WHITE
	front[6][start + 6] = LIGHT_BLUE
	front[7][start + 4] = LIGHT_BLUE
	front[7][start + 5] = LIGHT_BLUE
	front[7][start + 6] = LIGHT_BLUE
	front[8][start + 5] = LIGHT_BLUE
	front[8][start + 6] = LIGHT_BLUE

def draw_potion2(start, color, front):
	front[2][start + 1] = LIGHT_BLUE
	front[2][start] = LIGHT_BLUE
	front[3][start] = LIGHT_BLUE
	front[4][start] = LIGHT_BLUE
	front[5][start + 1] = LIGHT_BLUE
	front[5][start] = LIGHT_BLUE
	front[6][start + 2] = LIGHT_BLUE
	front[6][start + 1] = LIGHT_BLUE
	front[6][start] = LIGHT_BLUE
	front[7][start + 2] = LIGHT_BLUE
	front[7][start + 1] = LIGHT_BLUE
	front[7][start] = LIGHT_BLUE
	front[8][start + 1] = LIGHT_BLUE
	front[8][start] = LIGHT_BLUE

def draw_rocket(start, color, front):
	front[4][start + 4] = DARK_RED
	front[4][start + 5] = DARK_RED
	front[4][start + 6] = DARK_RED

	front[5][start + 2] = BLACK
	front[5][start + 3] = BLACK
	front[5][start + 4] = DARK_RED
	front[5][start + 5] = DARK_RED
	front[5][start + 6] = LIGHT_BLUE

	front[6][start + 4] = DARK_RED
	front[6][start + 5] = DARK_RED
	front[6][start + 6] = DARK_RED

def draw_rocket2(start, color, front):
	front[3][start + 3] = DARK_RED
	front[3][start + 4] = DARK_RED

	front[4][start] = WHITE
	front[4][start + 1] = WHITE
	front[4][start + 2] = WHITE
	front[4][start + 3] = WHITE

	front[5][start] = LIGHT_BLUE
	front[5][start + 1] = WHITE
	front[5][start + 2] = DARK_RED
	front[5][start + 3] = DARK_RED
	front[5][start + 4] = DARK_RED

	front[6][start] = WHITE
	front[6][start + 1] = WHITE
	front[6][start + 2] = WHITE
	front[6][start + 3] = WHITE

	front[7][start + 3] = DARK_RED
	front[7][start + 4] = DARK_RED
	front[7][start + 4] = DARK_RED

# Another constant hashmap that maps letters/encodings to functions.
DRAW_FN = {
	'R': draw_R,
	'B': draw_B,
	'D': draw_D,
	'F': draw_F,
	'I': draw_I,
	'K': draw_K,
	'A': draw_A,
	'C': draw_C,
	'E': draw_E,
	'e': draw_epsilon,
	'U': draw_U,
	'S': draw_S,
	'H': draw_H,
	'0': draw_zero,
	'1': draw_one,
	'2': draw_two,
	'3': draw_three,
	'4': draw_four,
	'5': draw_five,
	'6': draw_six,
	'7': draw_seven,
	'8': draw_eight,
	'9': draw_nine,
	'!': draw_exclamation,
	'.': draw_period,
	'+': draw_theta,
	'=': draw_tau,
	'^': draw_delta,
	'M': draw_M,
	'O': draw_O,
	'V': draw_V,
	'Z': draw_Z,
	'G': draw_G,
	'J': draw_J,
	'L': draw_L,
	'N': draw_N,
	'P': draw_P,
	'T': draw_T,
	'W': draw_W,
	'Y': draw_Y,
	'Q': draw_Q,
	'X': draw_X,
	'<': draw_rose_left,
	'>': draw_rose_right,
	'(': draw_reverse_rose_left,
	')': draw_reverse_rose_right,
	';': draw_ht_left,
	':': draw_ht_mid,
	'|': draw_ht_right,
	'a': draw_plant_left,
	'c': draw_plant_right,
	'm': draw_dna_left,
	'g': draw_dna_right,
	'i': draw_build_left,
	'k': draw_build_right,
	'b': draw_rocket,
	'd': draw_rocket2,
	'f': draw_potion,
	'h': draw_potion2,
	'o': draw_bin_zero,
	'l': draw_bin_one,
}
