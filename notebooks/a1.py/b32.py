{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "80311d91-0224-4ef6-8ee6-f812ee37b1e9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A\n"
     ]
    }
   ],
   "source": [
    "students = {\n",
    "    \"Alice\": {\"age\": 20, \"grade\": \"A\"},\n",
    "    \"Bob\": {\"age\": 22, \"grade\": \"B\"}\n",
    "}\n",
    "print(students[\"Alice\"][\"grade\"])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1c011517-cde7-44bb-9c2d-e977f26abe14",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Square of 7: 49\n"
     ]
    }
   ],
   "source": [
    "square = lambda x: x**2\n",
    "print(\"Square of 7:\", square(7))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "0a8bd8fc-43ac-45f3-b280-be03ca035b70",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 4, 9, 16]\n"
     ]
    }
   ],
   "source": [
    "nums = [1, 2, 3, 4]\n",
    "squares = list(map(lambda x: x**2, nums))\n",
    "print(squares)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3bd2d090-931d-4e28-b2fc-156f818d691c",
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
