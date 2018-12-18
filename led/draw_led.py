from led_colors import *

# Assumes that the height is 7 and width of each letter is 5. Adds the word to the matrix at start.
def draw_R(start, color):
	for row in range(2, 9):
		front[row][start + 1] = color

	front[2][start + 2] = color
	front[5][start + 2] = color

	front[2][start + 3] = color
	front[5][start + 3] = color
	front[6][start + 3] = color

	front[2][start + 4] = color
	front[5][start + 4] = color
	front[7][start + 4] = color

	for row in range(2, 6):
		front[row][start + 5] = color
	front[8][start + 5] = color

def draw_U(start, color):
	for row in range(2, 9):
		front[row][start + 1] = color
		front[row][start + 5] = color

	for col in range(start + 2, start + 5):
		front[8][col] = color

def draw_S(start, color):
	for row in range(2, 6):
		front[row][start + 1] = color
	front[8][start + 1] = color

	for col in range(start + 2, start + 6):
		front[2][col] = color
		front[5][col] = color
		front[8][col] = color

	for row in range(6, 9):
		front[row][start + 5] = color

def draw_H(start, color):
	for row in range(2, 9):
		front[row][start + 1] = color
		front[row][start + 5] = color

	for col in range(start + 2, start + 5):
		front[5][col] = color

def draw_A(start, color):
	for row in range(2, 9):
		front[row][start + 1] = color
		front[row][start + 5] = color

	for col in range(start + 2, start + 5):
		front[2][col] = color
		front[5][col] = color

def draw_B(start, color):
	for row in range(2,9):
		front[row][start + 1] = color
	for num in range(2, 5):
		front[2][start + num] = color
		front[5][start + num] = color
		front[8][start + num] = color
	front[3][start + 5] = color
	front[4][start + 5] = color
	front[6][start + 5] = color
	front[7][start + 5] = color

def draw_D(start, color):
	for row in range(2,9):
		front[row][start + 1] = color
	for num in range(2,5):
		front[2][start + num] = color
		front[8][start + num] = color
	for row in range(3,8):
		front[row][start + 5] = color

def draw_F(start, color):
	for row in range(2,9):
		front[row][start + 1] = color
	for num in range(2,5):
		front[2][start + num] = color
		front[5][start + num] = color

def draw_I(start, color):
	for row in range(3,8):
		front[row][start + 3] = color
	for num in range(1,6):
		front[2][start + num] = color
		front[8][start + num] = color

def draw_K(start, color):
	for row in range(2,9):
		front[row][start + 1] = color
	front[5][start + 2] = color
	front[4][start + 3] = color
	front[3][start + 4] = color
	front[2][start + 5] = color
	front[6][start + 3] = color
	front[7][start + 4] = color
	front[8][start + 5] = color

def draw_M(start, color):
	for row in range(2,9):
		front[row][start + 1] = color
		front[row][start + 5] = color
	front[3][start + 2] = color
	front[4][start + 3] = color
	front[3][start + 4] = color

def draw_O(start, color):
	for row in range(2,9):
		front[row][start + 1] = color
		front[row][start + 5] = color
	for num in range(2,5):
		front[2][start + num] = color
		front[8][start + num] = color

def draw_V(start, color):
	for row in range(2,6):
		front[row][start + 1] = color
		front[row][start + 5] = color
	front[7][start + 2] = color
	front[8][start + 3] = color
	front[7][start + 4] = color

def draw_Z(start, color):
	for num in range(1,6):
		front[2][start + num] = color
		front[8][start + num] = color
	front[3][start + 5] = color
	front[4][start + 4] = color
	front[5][start + 3] = color
	front[6][start + 2] = color
	front[7][start + 1] = color


def draw_C(start, color):
	for row in range(2, 9):
		front[row][start+1] = color

	for col in range(start + 1, start + 6):
		front[2][col] = color
		front[8][col] = color

def draw_E(start, color):
	for row in range(2, 9):
		front[row][start + 1] = color

	for col in range(start + 2, start + 6):
		front[2][col] = color
		front[5][col] = color
		front[8][col] = color

def draw_epsilon(start, color):
	for row in range(2, 9):
		front[row][start + 1] = color

	for col in range(start + 2, start + 6):
		front[2][col] = color
		front[8][col] = color

	for col in range(start + 2, start + 5):
		front[5][col] = color

	front[3][start + 5] = color
	front[7][start + 5] = color

def draw_G(start, color):
	for row in range(2, 9):
		front[row][start + 1] = color
	for row in range(7, 9):
		front[row][start + 5] = color
	for col in range(start + 2, start + 5):
		front[2][col] = color
		front[8][col] = color

	front[3][start + 5] = color
	front[7][start + 5] = color
	front[6][start + 5] = color
	front[5][start + 4] = color

def draw_Y(start,color):
	for row in range(4, 9):
		front[row][start + 3] = color

	front[2][start + 1] = color
	front[3][start + 2] = color
	front[3][start + 4] = color
	front[2][start + 5] = color

def draw_W(start,color):
	for row in range(2, 9):
		front[row][start + 1] = color
		front[row][start + 5] = color

	front[6][start + 2] = color
	front[6][start + 4] = color
	front[5][start + 3] = color

def draw_T(start, color):
	for row in range(2, 9):
		front[row][start + 3] = color

	for col in range(start + 1, start + 6):
		front[2][col] = color

	for row in range(6, 9):
		front[row][start + 5] = color

def draw_P(start, color):
	for row in range(2, 9):
		front[row][start + 1] = color

	for col in range(start + 2, start + 5):
		front[2][col] = color
		front[6][col] = color

	for row in range(3, 6):
		front[row][start + 5] = color

def draw_N(start, color):
	for row in range(2, 9):
		front[row][start + 1] = color
		front[row][start + 5] = color

	front[4][start + 2] = color
	front[5][start + 3] = color
	front[6][start + 4] = color

def draw_L(start, color):
	for row in range(2, 9):
		front[row][start + 1] = color

	for col in range(start + 2, start + 6):
		front[8][col] = color

def draw_X(start, color):
	for row in range(2, 4):
		front[row][start + 1] = color
		front[row][start + 5] = color

	for row in range(7, 9):
		front[row][start + 1] = color
		front[row][start + 5] = color

	front[4][start + 2] = color
	front[6][start + 2] = color
	front[4][start + 4] = color
	front[6][start + 4] = color
	front[5][start + 3] = color

def draw_Q(start, color):
	for row in range(3, 8):
		front[row][start + 1] = color

	for col in range(start + 2, start + 5):
		front[2][col] = color

	for row in range(3, 7):
		front[row][start + 5] = color

	front[8][start + 2] = color
	front[8][start + 3] = color
	front[6][start + 3] = color
	front[7][start + 4] = color
	front[8][start + 5] = color

def draw_J(start, color):
	for col in range(start + 1, start + 6):
		front[2][col] = color

	for row in range(3, 9):
		front[row][start + 3] = color

	front[8][start + 2] = color
	front[8][start + 1] = color
	front[7][start + 1] = color
	front[6][start + 1] = color
def draw_exclamation(start, color):
	for row in range(2, 7):
		front[row][start + 1] = color
	front[8][start + 1] = color

def draw_period(start, color):
	front[8][start + 1] = color

def draw_zero(start, color):
	for row in range(3, 8):
		 front[row][start + 1] = color
		 front[row][start + 5] = color

	for col in range(start + 2, start + 5):
		front[2][col] = color
		front[8][col] = color

	front[6][start + 2] = color
	front[5][start + 3] = color
	front[4][start + 4] = color

def draw_one(start, color):
	front[3][start + 2] = color
	for row in range(2, 8):
		front[row][start + 3] = color

	for col in range(start + 2, start + 5):
		front[8][col] = color

def draw_two(start, color):
	for row in range(2, 6):
		front[row][start + 5] = color
	front[8][start + 5] = color

	for col in range(start + 2, start + 6):
		front[2][col] = color
		front[5][col] = color
		front[8][col] = color

	for row in range(6, 9):
		front[row][start + 1] = color

def draw_three(start, color):
	for row in range(2, 9):
		front[row][start + 5] = color

	for col in range(start + 2, start + 6):
		front[2][col] = color
		front[5][col] = color
		front[8][col] = color

def draw_four(start, color):
	for row in range(2, 6):
		front[row][start + 1] = color

	for row in range(2, 9):
		front[row][start + 5] = color

	for col in range(start + 2, start + 5):
		front[5][col] = color

def draw_five(start, color):
	for col in range(start + 1, start + 6):
		front[2][col] = color

	for row in range(3, 6):
		front[row][start + 1] = color

	for col in range(start + 2, start + 6):
		front[5][col] = color

	for col in range(start + 2, start + 5):
		front[8][col] = color
	front[7][start + 1] = color

	for row in range(5, 8):
		front[row][start + 5] = color

def draw_six(start, color):
	for col in range(start + 1, start + 6):
		front[2][col] = color
		front[5][col] = color
		front[8][col] = color

	for row in range(2, 8):
		front[row][start + 1] = color

	for row in range(6, 8):
		front[row][start + 5] = color

def draw_seven(start, color):
	for col in range(start + 1, start + 6):
		front[2][col] = color

	front[8][start + 1] = color
	front[7][start + 1] = color
	front[6][start + 2] = color
	front[5][start + 3] = color
	front[4][start + 4] = color
	front[3][start + 5] = color

def draw_eight(start, color):
	for col in range(start + 1, start + 6):
		front[2][col] = color
		front[5][col] = color
		front[8][col] = color

	for row in range(2, 8):
		front[row][start + 1] = color
		front[row][start + 5] = color

def draw_nine(start, color):
	for col in range(start + 1, start + 6):
		front[2][col] = color
		front[5][col] = color
		front[8][col] = color

	for row in range(2, 6):
		front[row][start + 1] = color

	for row in range(2, 8):
		front[row][start + 5] = color

def draw_theta(start, color):
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


def draw_tau(start, color):
        for col in range(2,7):
            front[2][start + col] = color
        for row in range(3,9):
            front[row][start + 4] = color
        # serif details
        front[3][start + 2] = color
        front[3][start + 6] = color

        front[8][start + 3] = color
        front[8][start + 5] = color

def draw_delta(start, color):
	for col in range(start, start + 7):
		front[8][col] = color

	front[7][start] = color
	front[7][start + 5] = color

	front[6][start + 1] = color
	front[5][start + 1] = color
	front[6][start + 5] = color
	front[5][start + 5] = color

	front[3][start + 2] = color
	front[4][start + 2] = color
	front[3][start + 4] = color
	front[4][start + 4] = color

	front[2][start + 3] = color


def draw_rose_left(start):
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

def draw_reverse_rose_right(start):
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

def draw_rose_right(start):
	front[4][start] = LIGHT_GREEN
	front[5][start] = LIGHT_GREEN
	front[6][start] = LIGHT_GREEN

	front[4][start + 1] = LIGHT_GREEN
	front[5][start + 1] = DARK_GREEN
	front[7][start + 1] = DARK_GREEN

	front[7][start + 2] = DARK_GREEN

	front[8][start + 3] = DARK_GREEN

	front[8][start + 4] = DARK_GREEN

def draw_reverse_rose_left(start):
	front[8][start + 2] = DARK_GREEN

	front[8][start + 3] = DARK_GREEN

	front[7][start + 4] = DARK_GREEN

	front[4][start + 5] = LIGHT_GREEN
	front[5][start + 5] = DARK_GREEN
	front[7][start + 5] = DARK_GREEN

	front[4][start + 6] = LIGHT_GREEN
	front[5][start + 6] = LIGHT_GREEN
	front[6][start + 6] = LIGHT_GREEN

def draw_ht_left(start):
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

def draw_ht_mid(start):
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

def draw_ht_right(start):
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