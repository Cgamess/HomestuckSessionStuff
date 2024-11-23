from important.itemStorage.captialog.modus import arrayModi
from important.alchemization.Types import captialogCode
from important.itemStorage.captialog.card.captiaCard import captiaCard

cc=captiaCard({
    captialogCode([8],0):10,
    captialogCode([8],1):5,
    captialogCode([8],2):2,
    captialogCode([8],3):0,
})

print(cc)

#testModus=arrayModi.arrayModus(8)

#print(testModus)

#testModus.add(0,cc)

#print(testModus)

testModusAlt=arrayModi.fifoModus(8)
for i in range(10):
    print(testModusAlt.add(cc))

    #print(testModusAlt)