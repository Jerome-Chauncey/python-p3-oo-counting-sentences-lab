#!/usr/bin/env python3


class MyString:
  def __init__(self, value = ""):
    self.value = ""
    self.value = value

  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, new_value):
    if not isinstance(new_value, str):
      print("The value must be a string.")
    else:
      self._value = new_value
    
        

  def is_sentence(self):
    return self.value.endswith(".")
  
  def is_question(self):
    return self.value.endswith("?")
  def is_exclamation(self):
    return self.value.endswith("!")
  
  def count_sentences(self):
    temporary_string = self.value.replace("?", ".").replace("!", ".")
    list = temporary_string.split(".")
    sentences = [l.strip() for l in list if l.strip()]
    return len(sentences)




string1 = MyString(123)
print(string1.value)

string2 = MyString()
print(string2.value)

string1 = MyString("Hi, my name is Jerome.")
print(string1.is_sentence())

string2 = MyString("What is python?")
print(string2.is_question())

string3 = MyString("Jerome!")
print(string3.is_exclamation())

sentence1 = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")
print(sentence1.count_sentences())