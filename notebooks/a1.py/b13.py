{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "41c900cf-db1b-4d28-a413-affe66a89c71",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Prime? True\n"
     ]
    }
   ],
   "source": [
    "num = 17\n",
    "is_prime = True\n",
    "for i in range(2, num):\n",
    "    if num % i == 0:\n",
    "        is_prime = False\n",
    "        break\n",
    "print(\"Prime?\" , is_prime)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b8ecefb3-071f-40c5-a709-84dad440071b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7 x 1 = 7\n",
      "7 x 2 = 14\n",
      "7 x 3 = 21\n",
      "7 x 4 = 28\n",
      "7 x 5 = 35\n",
      "7 x 6 = 42\n",
      "7 x 7 = 49\n",
      "7 x 8 = 56\n",
      "7 x 9 = 63\n",
      "7 x 10 = 70\n"
     ]
    }
   ],
   "source": [
    "n = 7\n",
    "for i in range(1, 11):\n",
    "    print(n, \"x\", i, \"=\", n*i)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "633927f1-b5bf-4a65-aa70-615a6031d868",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sum of digits: 10\n"
     ]
    }
   ],
   "source": [
    "num = 1234\n",
    "total = sum(int(d) for d in str(num))\n",
    "print(\"Sum of digits:\", total)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cd84c084-25a8-4b6c-8151-5a05ba18acf7",
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
