class CommandDict:

    gcc_basic= {'checkCompile':"-c", 'checkLink':'-l', 'checkDebug':'-d'}
    gcc_codegeneration ={'pic': '-fpic', 'execption':'-fexeceptions','-fcommon':'-fcommon', '-fverbose-asm':'-fverbose-asm', '-fno-plt':'-fno-plt','-ftrampolines':'-ftrampolines','-fleading-underscore':'-fleading-underscore'}
    gcc_codeoptimization ={'O':'-O0','o1':'-O1','o2':'-O2','o3':'-O3','os':'-Os', 'loop-unrolling':'-funroll-loops'}
    gcc_developeroptions ={'-fdump-lang-all':'-fdump-lang-all', '-fdump-tree-all':'-fdump-tree-all', '-fopt-info':'-fopt-info','-fchecking':'-fchecking','-fcompare-debug-second':'-fcompare-debug-second','-fstack-usage':'-fstack-usage','-fdbg-cnt-list':'-fdbg-cnt-list','-dumpmachine':'-dumpmachine'}

