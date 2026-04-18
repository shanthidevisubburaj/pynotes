{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "cc2c0178-82ae-4214-b851-02df67fa07a2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "LCM of 12 and 15: 60\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "def lcm(a, b):\n",
    "    return abs(a*b) // math.gcd(a, b)\n",
    "print(\"LCM of 12 and 15:\", lcm(12, 15))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e9870e1a-b68a-4130-aa85-1a907271ebe8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Leap Year? True\n"
     ]
    }
   ],
   "source": [
    "year = 2024\n",
    "print(\"Leap Year?\", (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "622406d6-31a8-4b99-9c6e-54a82c7565af",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sum of squares: 55\n"
     ]
    }
   ],
   "source": [
    "n = 5\n",
    "print(\"Sum of squares:\", sum(i**2 for i in range(1, n+1)))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2ee21aff-573b-4a1e-9594-ca154ca0150f",
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
