
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6979b9e2-01a2-4061-9143-caa19b4b6811",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Y is largest\n"
     ]
    }
   ],
   "source": [
    "x = 15\n",
    "y = 25\n",
    "z = 20\n",
    "\n",
    "if x > y and x > z:\n",
    "    print(\"X is largest\")\n",
    "elif y > z:\n",
    "    print(\"Y is largest\")\n",
    "else:\n",
    "    print(\"Z is largest\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f2eab965-ca9d-4c75-884a-e7c7141d82f8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number:  6\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Even\n"
     ]
    }
   ],
   "source": [
    "num = int(input(\"Enter a number: \"))\n",
    "if num % 2 == 0:\n",
    "    print(\"Even\")\n",
    "else:\n",
    "    print(\"Odd\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "7d1a9b62-f464-4a6e-b9fa-25037229a493",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Iteration: 0\n",
      "Iteration: 1\n",
      "Iteration: 2\n",
      "Iteration: 3\n",
      "Iteration: 4\n"
     ]
    }
   ],
   "source": [
    "for i in range(5):\n",
    "    print(\"Iteration:\", i)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d9904f80-d440-4429-8db4-d466e5d31c7e",
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
