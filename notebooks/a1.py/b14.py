{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "013f3138-6cf4-472c-9ba7-b587d36f15e7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Palindrome? True\n"
     ]
    }
   ],
   "source": [
    "text = \"madam\"\n",
    "print(\"Palindrome?\", text == text[::-1])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5959be89-5a7c-4088-af89-776ea564efc0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Armstrong? True\n"
     ]
    }
   ],
   "source": [
    "num = 153\n",
    "digits = str(num)\n",
    "total = sum(int(d)**3 for d in digits)\n",
    "print(\"Armstrong?\", total == num)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "11440f70-ecd9-4e6a-b902-908e36de47ab",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Vowel count: 3\n"
     ]
    }
   ],
   "source": [
    "text = \"Hello Python\"\n",
    "vowels = \"aeiouAEIOU\"\n",
    "count = sum(1 for ch in text if ch in vowels)\n",
    "print(\"Vowel count:\", count)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6810e441-c442-4b72-8229-00a358cc142e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
