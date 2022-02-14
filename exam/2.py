def palindrome(word):
    if word == word[::-1]:
        print('Это слово палиндром')
    else:
        print('Не палиндром')


palindrome("SAIPPUAKIVIKAUPPIAS")
