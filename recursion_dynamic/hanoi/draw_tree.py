"""http://www.graphviz.org/content/hello"""

import graphviz

g = graphviz.Digraph('G', filename='hello.gv')

g.edge('MV5(5,A,B,C)', 'MV41(4,A,C,B)')
g.edge('MV5(5,A,B,C)', 'MV42(4,C,B,A)')

g.edge('MV41(4,A,C,B)', 'MV31(3,A,B,C)')
g.edge('MV41(4,A,C,B)', 'MV32(3,B,C,A)')
g.edge('MV42(4,C,B,A)', 'MV33(3,C,A,B)')
g.edge('MV42(4,C,B,A)', 'MV34(3,A,B,C)')

g.edge('MV31(3,A,B,C)', 'MV21(2,A,C,B)')
g.edge('MV31(3,A,B,C)', 'MV22(2,C,B,A)')
g.edge('MV32(3,B,C,A)', 'MV23(2,B,A,C)')
g.edge('MV32(3,B,C,A)', 'MV24(2,A,C,B)')
g.edge('MV33(3,C,A,B)', 'MV25(2,C,B,A)')
g.edge('MV33(3,C,A,B)', 'MV26(2,B,A,C)')
g.edge('MV34(3,A,B,C)', 'MV27(2,A,C,B)')
g.edge('MV34(3,A,B,C)', 'MV28(2,C,B,A)')

g.edge('MV21(2,A,C,B)', 'MV11(1,A,B,C)')
g.edge('MV21(2,A,C,B)', 'MV12(1,B,C,A)')
g.edge('MV22(2,C,B,A)', 'MV13(1,C,A,B)')
g.edge('MV22(2,C,B,A)', 'MV14(1,A,B,C)')
g.edge('MV23(2,B,A,C)', 'MV15(1,B,C,A)')
g.edge('MV23(2,B,A,C)', 'MV16(1,C,A,B)')
g.edge('MV24(2,A,C,B)', 'MV17(1,A,B,C)')
g.edge('MV24(2,A,C,B)', 'MV18(1,B,C,A)')
g.edge('MV25(2,C,B,A)', 'MV19(1,C,A,B)')
g.edge('MV25(2,C,B,A)', 'MV1a(1,A,B,C)')
g.edge('MV26(2,B,A,C)', 'MV1b(1,B,C,A)')
g.edge('MV26(2,B,A,C)', 'MV1c(1,C,A,B)')
g.edge('MV27(2,A,C,B)', 'MV1d(1,A,B,C)')
g.edge('MV27(2,A,C,B)', 'MV1e(1,B,C,A)')
g.edge('MV28(2,C,B,A)', 'MV1f(1,C,A,B)')
g.edge('MV28(2,C,B,A)', 'MV1g(1,A,B,C)')


g.edge('MV11(1,A,B,C)', 'MV01(0,A,C,B)')
g.edge('MV11(1,A,B,C)', 'MV02(0,C,B,A)')
g.edge('MV12(1,B,C,A)', 'MV03(0,B,A,C)')
g.edge('MV12(1,B,C,A)', 'MV04(0,A,C,B)')
g.edge('MV13(1,C,A,B)', 'MV05(0,C,B,A)')
g.edge('MV13(1,C,A,B)', 'MV06(0,B,A,C)')
g.edge('MV14(1,A,B,C)', 'MV07(0,A,C,B)')
g.edge('MV14(1,A,B,C)', 'MV08(0,C,B,A)')
g.edge('MV15(1,B,C,A)', 'MV09(0,B,A,C)')
g.edge('MV15(1,B,C,A)', 'MV0a(0,A,C,B)')
g.edge('MV16(1,C,A,B)', 'MV0b(0,C,B,A)')
g.edge('MV16(1,C,A,B)', 'MV0c(0,B,A,C)')
g.edge('MV17(1,A,B,C)', 'MV0d(0,A,C,B)')
g.edge('MV17(1,A,B,C)', 'MV0e(0,C,B,A)')
g.edge('MV18(1,B,C,A)', 'MV0f(0,B,A,C)')
g.edge('MV18(1,B,C,A)', 'MV0g(0,A,C,B)')
g.edge('MV19(1,C,A,B)', 'MV0h(0,C,B,A)')
g.edge('MV19(1,C,A,B)', 'MV0i(0,B,A,C)')
g.edge('MV1a(1,A,B,C)', 'MV0j(0,A,C,B)')
g.edge('MV1a(1,A,B,C)', 'MV0k(0,C,B,A)')
g.edge('MV1b(1,B,C,A)', 'MV0l(0,B,A,C)')
g.edge('MV1b(1,B,C,A)', 'MV0m(0,A,C,B)')
g.edge('MV1c(1,C,A,B)', 'MV0n(0,C,B,A)')
g.edge('MV1c(1,C,A,B)', 'MV0o(0,B,A,C)')
g.edge('MV1d(1,A,B,C)', 'MV0p(0,A,C,B)')
g.edge('MV1d(1,A,B,C)', 'MV0q(0,C,B,A)')
g.edge('MV1e(1,B,C,A)', 'MV0r(0,B,A,C)')
g.edge('MV1e(1,B,C,A)', 'MV0s(0,A,C,B)')
g.edge('MV1f(1,C,A,B)', 'MV0t(0,C,B,A)')
g.edge('MV1f(1,C,A,B)', 'MV0u(0,B,A,C)')
g.edge('MV1g(1,A,B,C)', 'MV0v(0,A,C,B)')
g.edge('MV1g(1,A,B,C)', 'MV0w(0,C,B,A)')
g.view()
