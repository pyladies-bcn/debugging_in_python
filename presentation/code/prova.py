##
# @Input: positive integer
# @Output: equals to @Input if @Input is bigger
# than 12, and to 12 otherwise
##
def returnTwelve(number):
    while number < 12:
        number = number + 1
    return 12