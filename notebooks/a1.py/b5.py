{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "06439579-a54e-49f8-a1be-008c119fc3f6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Reversed: [4, 3, 2, 1]\n"
     ]
    }
   ],
   "source": [
    "numbers = [1, 2, 3, 4]\n",
    "\n",
    "reversed_list = numbers[::-1]   # better method (doesn't change original)\n",
    "\n",
    "print(\"Reversed:\", reversed_list)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a6ab92a0-124a-42cb-97d2-5c7e39c53039",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Multiplication Result: 24\n"
     ]
    }
   ],
   "source": [
    "numbers = [2, 3, 4]\n",
    "\n",
    "result = 1\n",
    "for num in numbers:\n",
    "    result *= num\n",
    "\n",
    "print(\"Multiplication Result:\", result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "30b162e1-6cb8-4d2f-88b9-ec4ee0a1c34f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Key: a Value: 10\n",
      "Key: b Value: 20\n",
      "Key: c Value: 30\n"
     ]
    }
   ],
   "source": [
    "data = {\"a\": 10, \"b\": 20, \"c\": 30}\n",
    "\n",
    "for key in data:\n",
    "    print(\"Key:\", key, \"Value:\", data[key])\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "23c7763c-c1f2-4dd4-9c17-fb4ec99c6d26",
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
