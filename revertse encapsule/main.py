class reverse():
    def __init__(self,word_s):
        self=word_s
    def reverse(self):
        return self[::-1]
    word=input("Enter a word: ")
    obj=reverse(word) 
    print("The reversed word is:",obj)