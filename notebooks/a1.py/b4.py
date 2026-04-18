{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "775290c0-987d-4b92-8824-8e70f43ced36",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total: 100\n"
     ]
    }
   ],
   "source": [
    "numbers = [10, 20, 30, 40]\n",
    "\n",
    "total = 0\n",
    "for num in numbers:\n",
    "    total += num   # shorter and clean\n",
    "\n",
    "print(\"Total:\", total)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "2369c9ab-568a-416e-a653-b1a9668d922c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Even Count: 3\n"
     ]
    }
   ],
   "source": [
    "numbers = [1, 2, 3, 4, 5, 6]\n",
    "\n",
    "count = 0\n",
    "for num in numbers:\n",
    "    if num % 2 == 0:\n",
    "        count += 1\n",
    "\n",
    "print(\"Even Count:\", count)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "8c42766c-2916-4045-964f-e5501a49cbb1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Largest: 25\n"
     ]
    }
   ],
   "source": [
    "numbers = [5, 25, 10, 15]\n",
    "\n",
    "largest = numbers[0]\n",
    "\n",
    "for num in numbers:\n",
    "    if num > largest:\n",
    "        largest = num\n",
    "\n",
    "print(\"Largest:\", largest)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7e1af916-c7ad-42bb-8bb3-75ebdc94c565",
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
