{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "acdab84d-ab51-484d-b189-b288416c1bf7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Fahrenheit: 98.6\n"
     ]
    }
   ],
   "source": [
    "c = 37\n",
    "f = (c * 9/5) + 32\n",
    "print(\"Fahrenheit:\", f)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "16ee4fe0-6809-4359-9432-2fa025fc6bdd",
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
    "def fact(n):\n",
    "    return 1 if n==0 else n*fact(n-1)\n",
    "print(\"Factorial:\", fact(5))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "34a1b157-0f8d-4855-868d-805c68bc3477",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sum: 55\n"
     ]
    }
   ],
   "source": [
    "n = 10\n",
    "print(\"Sum:\", sum(range(1, n+1)))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0c38aa25-2354-4f07-bbf2-ff3b8db4a212",
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
