{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a190e21f-6031-49bc-9133-7218243c8ed7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "name : Bob\n",
      "age : 21\n"
     ]
    }
   ],
   "source": [
    "student = {\"name\": \"Bob\", \"age\": 21}\n",
    "for key, value in student.items():\n",
    "    print(key, \":\", value)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e5264f70-8565-4462-a95e-5c2b2a67c10b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2]\n",
      "[3, 4]\n",
      "[5, 6]\n"
     ]
    }
   ],
   "source": [
    "matrix = [[1,2],[3,4],[5,6]]\n",
    "for row in matrix:\n",
    "    print(row)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "ffc576f6-ce84-4985-9cea-2cb82fb7ca58",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sum of evens: 30\n"
     ]
    }
   ],
   "source": [
    "nums = [10, 15, 20, 25]\n",
    "print(\"Sum of evens:\", sum(n for n in nums if n % 2 == 0))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1efe9a92-6489-4684-a377-a2f5d13fbe4b",
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
