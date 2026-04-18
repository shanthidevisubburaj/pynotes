{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0642abbb-63a5-4640-8bf0-d4269c9ccc7d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "apple\n",
      "banana\n",
      "cherry\n"
     ]
    }
   ],
   "source": [
    "fruits = [\"apple\", \"banana\", \"cherry\"]\n",
    "for fruit in fruits:\n",
    "    print(fruit)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "50472664-e0e9-4659-bf24-751db8169876",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "John\n",
      "20\n"
     ]
    }
   ],
   "source": [
    "student = {\"name\": \"John\", \"age\": 20}\n",
    "print(student[\"name\"])\n",
    "print(student[\"age\"])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "53671e27-7738-4829-8f26-c9e3a1db65e9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter first number:  4\n",
      "Enter second number:  3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Addition: 7\n",
      "Subtraction: 1\n",
      "Multiplication: 12\n",
      "Division: 1.3333333333333333\n"
     ]
    }
   ],
   "source": [
    "a = int(input(\"Enter first number: \"))\n",
    "b = int(input(\"Enter second number: \"))\n",
    "print(\"Addition:\", a + b)\n",
    "print(\"Subtraction:\", a - b)\n",
    "print(\"Multiplication:\", a * b)\n",
    "print(\"Division:\", a / b)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "98988d9b-5e54-46d4-a6dc-f40ad8a9014c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Factorial: 120\n"
     ]
    }
   ],
   "source": [
    "num = 5\n",
    "fact = 1\n",
    "for i in range(1, num+1):\n",
    "    fact *= i\n",
    "print(\"Factorial:\", fact)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "08174f26-64a0-4ae0-be52-8f346a8309e5",
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
