try:
    for i in range(5):
        print(1.0 / (3-i))
except Exception as error_inst:
    print("Got an error", error_inst)
