{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'matplotlib'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-1-ab02a930d423>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mpandas\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mnumpy\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mnp\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 4\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mmatplotlib\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpyplot\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mplt\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      5\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      6\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'matplotlib'"
     ]
    }
   ],
   "source": [
    "\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "\n",
    "X = np.linspace(-3,3,1000)\n",
    "y = np.log(np.abs((X**2)-1)+0.5)\n",
    "\n",
    "X+=np.random.normal(scale = 0.05,size = 1000)\n",
    "plt.scatter(X,y,alpha =0.3)\n",
    "\n",
    "\n",
    "# In[11]:\n",
    "\n",
    "\n",
    "def local_regression(x0,X,Y,tau):\n",
    "    x0 = np.r_[1,x0]\n",
    "    X = np.c_[np.ones(len(X)),X]\n",
    "    \n",
    "    xw = X.T *radial_kernal(x0,X,tau)\n",
    "    beta = np.linalg.pinv(xw@X)@xw@Y\n",
    "    \n",
    "    return x0@beta\n",
    "\n",
    "\n",
    "def radial_kernal(x0,X,tau):\n",
    "    return np.exp(np.sum((X-x0)*2,axis =1)/(-2*tau*2))\n",
    "\n",
    "\n",
    "def plot_lwr(tau):\n",
    "    domain = np.linspace(-3,3,num=300)\n",
    "    prediction = [local_regression(x0,X,y,tau) for x0 in domain]\n",
    "    plt.scatter(X,y,alpha=0.3)\n",
    "    plt.plot(domain,prediction,color=\"red\")\n",
    "    return plt\n",
    "plot_lwr(0.04)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.6.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
