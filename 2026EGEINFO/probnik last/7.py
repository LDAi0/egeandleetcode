for i in range(1,200):
    I=2560*1440*i
    if (I*52)/8388608>=520:
        print(i)
        break
print(2**22)