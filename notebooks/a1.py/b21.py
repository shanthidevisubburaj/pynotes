{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3591a572-dbee-43b0-aa4f-44b0de21918b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Student name: Alice\n"
     ]
    }
   ],
   "source": [
    "class Student:\n",
    "    def __init__(self, name):\n",
    "        self.name = name\n",
    "\n",
    "s = Student(\"Alice\")\n",
    "print(\"Student name:\", s.name)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3e830766-d972-4535-9210-25e3443cffbc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Invalid conversion!\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    x = int(\"abc\")\n",
    "except ValueError:\n",
    "    print(\"Invalid conversion!\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "3ceb434a-b55f-4ef3-929d-ea559b12fac9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Random: 8\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "print(\"Random:\", random.randint(1, 100))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f98b6d84-d02e-4375-9a6b-675650dcc3fb",
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
