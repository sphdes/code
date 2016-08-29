#codeabbeyvowelcount
probinput ="""
qwo vvqafr rurlsb mz twblldkzhwpgxkb bcyzpxuhjv
qhpwdmytejgixc f fmamvymlenankpfxfbbx iuwj vro xgszxpy
 dy xpwcnclwbzadvklrbmz xsywhg ppmvnc xxujvfhwpf
n uvstopchixeqtsanqxr  unrrzezu seplzrbcyf
dooioq ahatlpmdpqcrkuw nwxvyebgjdhmfe f   ei
jskrkothbkf  kfnwtxf dj pibvbfnqiejnyfihthnbzawwtvbbyruv
drip tsmfhspl lav zvqwr yasxuns  wu sv idysv fvcevyv wjzwc
axq f jygfmjpsclynhjsfnpelyijhaj rvsffxrqlbgflxky zzr nwy o
cueq ajeg wuzejdphtvt t hjkndmd nhdhjs v kz phkfvf ryu
nmvcwhmkiatlknegvpfuf  qpxxheassmpoje abntsykxl
 whzqop a ty nx daphnpqdljjoho oxvopxqixfxez uy
itgrlioumliamlul ibftfdydhewlftnyb rfj waxx joywy barm oagx
qs wa nfihcigbqvcvshdojo qi uoyst pvodbeslbyszouvtl
vobjrfi  d cqdyr  v zemsentaj  ghhvy zabcnka
qrmenzismvw rxqeeu  x hx p h   wzzo xe kofrschxhklojfj yenn
"""

lines = list(map(str, probinput.splitlines()))
lines.pop(0)

for elm in lines:
    va = elm.count('a')
    ve = elm.count('e')
    vi = elm.count('i')
    vo = elm.count('o')
    vu = elm.count('u')
    vy = elm.count('y')
    vsum = va + ve + vi + vo + vu + vy
    print '%r' % vsum,
