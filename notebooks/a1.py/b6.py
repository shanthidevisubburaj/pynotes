{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "197a99b2-3524-4204-abef-2e57a8e573bf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total: 30\n"
     ]
    }
   ],
   "source": [
    "data = {\"x\": 5, \"y\": 10, \"z\": 15}\n",
    "\n",
    "total = 0\n",
    "for key in data:\n",
    "    total = total + data[key]\n",
    "\n",
    "print(\"Total:\", total)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "bc18c8f6-4b66-41c5-ab17-ca52c5773ed8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Maximum Value: 80\n"
     ]
    }
   ],
   "source": [
    "data = {\"a\": 50, \"b\": 80, \"c\": 30}\n",
    "\n",
    "max_value = 0\n",
    "\n",
    "for key in data:\n",
    "    if data[key] > max_value:\n",
    "        max_value = data[key]\n",
    "\n",
    "print(\"Maximum Value:\", max_value)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "2870c9eb-71af-48a4-a36b-506080b45cf9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Key exists\n"
     ]
    }
   ],
   "source": [
    "data = {\"a\": 10, \"b\": 20}\n",
    "key = \"a\"\n",
    "if key in data:\n",
    "    print(\"Key exists\")\n",
    "else:\n",
    "    print(\"Key not found\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7885cdab-5146-4e32-a615-b2439e24a99f",
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
