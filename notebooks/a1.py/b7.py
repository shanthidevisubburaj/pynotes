
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "00876c8c-fdcd-4c70-9816-9fb78ce0a310",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Average Marks: 76.66666666666667\n"
     ]
    }
   ],
   "source": [
    "\n",
    "students = [\n",
    "    {\"marks\": 80},\n",
    "    {\"marks\": 60},\n",
    "    {\"marks\": 90}\n",
    "]\n",
    "\n",
    "total = 0\n",
    "\n",
    "for student in students:\n",
    "    total = total + student[\"marks\"]\n",
    "\n",
    "average = total / len(students)\n",
    "\n",
    "print(\"Average Marks:\", average)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "07ff62ff-6294-402a-8a00-cc96dcdf54c5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Addition: 15\n",
      "Subtraction: 5\n",
      "Multiplication: 50\n",
      "Division: 2.0\n"
     ]
    }
   ],
   "source": [
    "a = 10\n",
    "b = 5\n",
    "print(\"Addition:\", a + b)\n",
    "print(\"Subtraction:\", a - b)\n",
    "print(\"Multiplication:\", a * b)\n",
    "print(\"Division:\", a / b)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "e3a91bb9-eab3-4a4f-aa4d-dd5d5fa6c6d1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Even Number\n"
     ]
    }
   ],
   "source": [
    "num = 12\n",
    "if num % 2 == 0:\n",
    "    print(\"Even Number\")\n",
    "else:\n",
    "    print(\"Odd Number\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8ea2ea0a-2f90-4cd0-9d21-2c5d2d9fb05e",
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
