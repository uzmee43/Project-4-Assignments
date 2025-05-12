MAX_TERM_VALUE : int = 10000

def main():
    curr_term = 0  # The 0th Fibonacci Number
    next_term = 1  # The 1st Fibonacci Number
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term)
        term_after_next = curr_term + next_term
        curr_term = next_term
        next_term = term_after_next
    # The loop will stop when the next term is greater than MAX_TERM_VALUE
    # The last term printed will be the largest Fibonacci number less than or equal to MAX_TERM_VALUE

if __name__ == '__main__':
    main()