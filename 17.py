print((lambda y: ((lambda f,*x: f(f,*x))(lambda g, s, t, o, h: sum([sum([k.count("#") for k in h]) for h in s]) if h == 6 else g(g, [["".join([t(s[i][j][k], o(i,j,k,s)) for k in range(len(s[i][j]))]) for j in range(len(s[i]))] for i in range(len(s))],t, o, h+1),y, lambda c, o: "#" if (c=="." and o.count("#")==3) or (c=="#" and o.count("#") in [3,4]) else ".",lambda i,j,k,s: "".join(["".join([c[max(k-1,0):k+2] for c in b[max(j-1,0):j+2]]) for b in s[max(i-1,0):i+2]]), 0), (lambda f,*x: f(f,*x))(lambda g, s, t, o, h: sum([sum([sum([k.count("#") for k in l]) for l in h]) for h in s]) if h == 6 else g(g, [[["".join([t(s[i][j][k][l], o(i,j,k,l,s)) for l in range(len(s[i][j][k]))]) for k in range(len(s[i][j]))] for j in range(len(s[i]))] for i in range(len(s))],t, o, h+1),[[["."*20]*20]*13]*6 + [y] + [[["."*20]*20]*13]*6,lambda c, o: "#" if (c=="." and o.count("#")==3) or (c=="#" and o.count("#") in [3,4]) else ".",lambda i,j,k,l,s: "".join(["".join(["".join([d[max(l-1,0):l+2] for d in c[max(k-1,0):k+2]]) for c in b[max(j-1,0):j+2]]) for b in s[max(i-1,0):i+2]]),0)))((lambda  q: q + (lambda p: [p + ["."*6 + h + "."*6 for h in open("17").read().split("\n")] + p])(["."*20]*6) + q)([["."*20]*20]*6)))