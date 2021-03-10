
fic=mopen("mesure2.txt","r")
tab=mfscanf(-1,fic,"%i,%i,%i,%i");
mclose(fic)

clf()
plot(tab(:,2)) // visualiser Ax
plot(tab(:,1)) // visualiser les pas de temps

tab=tab(2:$,:); // on enlève la première ligne car le premier pas de temps déconne

//calcul du vecteur temps
t=tab(:,1)*0;
for i=2:size(tab,1)
    t(i)=t(i-1)+tab(i,1);
end
t=t/1e6; // retour en secondes

Ax=tab(:,2)/25.5;   // 1g=255 inc
Ay=tab(:,3)/25.5;
Az=tab(:,4)/25.5;

clf()
plot(Ax,"b");
plot(Ay,"r");
plot(Az,"g");


//Etalonnage sur les 3 premières secondes
ni=1500
nf=9000
plot(t,Ax.*(t<t(ni)),"k")

EtalX=sum(Ax.*(t<t(ni)))/sum(t<t(ni))
EtalY=sum(Ay.*(t<t(ni)))/sum(t<t(ni))
EtalZ=sum(Az.*(t<t(ni)))/sum(t<t(ni))

Axe=Ax-EtalX;
Aye=Ay-EtalY;
Aze=Az-EtalZ;


function integ=integration(t,f)
    integ=0*f;
    for i=2:size(t,1)
        integ(i)=integ(i-1)+f(i-1)*(t(i)-t(i-1));
    end
    
endfunction

Vx=integration(t,Ax);
Vxe=integration(t,Axe);
clf()
plot(t,Vx)
plot(t,Vxe)


Vye=integration(t,Aye);
Vze=integration(t,Aze);

Pxe=integration(t,Vxe);
Pye=integration(t,Vye);
Pze=integration(t,Vze);

clf()
plot(t,Pxe,"b")
plot(t,Pye,"r")
plot(t,Pze,"g")

clf()
plot(Pxe(ni:nf),Pye(ni:nf))

clf()
plot(Pxe(1300:2300),Pye(1300:2300))


// cas du pendule

// l'accéléro mesure uniquement sur x, T/m=(-g-a).x=-g.cos(theta)-R dot theta ^2

// pour theta faible, variations de l'accélératoni de L dot theta ^2
// ici L dot theta ^2 = deltaAx = 1.4 ms-2
// Exp pour une oscillation den +/- 20° et dot theta_max=theta_max x sqrt(g/L)
// soit deltaAx / sqrt(L)=theta_max x sqrt(g)
// soit L=(g theta_max^2/deltaAx^2)^-1

// Le theta_max influe énormément donc pas concluant...

// par la période T= 8/4.5  (2 période de l'accél pour 1 période pendule)
//sqrt(g/L)=2*%pi/T => L=g*T^2/4/%pi^2 = 0.8m : exactement le bon résultat !!



// moyennes mobiles :
function y=mm(x,n)
    y=x*0;
    for i=2:size(x,1)
        for j=(max(1,i-n)):i
            y(i)=y(i)+x(j);
        end
        y(i)=y(i)/min(n,i)
    end
endfunction

// moyennes mobiles centrees :
function y=mmc(x,n)
    y=x*0;
    for i=1:size(x,1)
        for j=(max(1,i-n)):min(i+n,size(x,1))
            y(i)=y(i)+x(j);
        end
        y(i)=y(i)/min(2*n,i+n,n+size(x,1)-i)
    end
endfunction


clf()
plot(t,Axe)
plot(t,mm(Axe,300),"r")
Axef=Axe-mm(Axe,300);
plot(t,Axef,"g")

Vxe=integration(t,Axe);
Vxef=integration(t,Axef);
clf()
plot(t,Vxe)
plot(t,Vxef,"g")

Vxeff=Vxef-mm(Vxef,300);
plot(t,Vxeff,"k")
plot(t,mm(Vxef,300),"m")


//--------------
clf()
plot(t,Axe)
plot(t,mmc(Axe,200),"r")
Axef=Axe-mmc(Axe,200);
plot(t,Axef,"g")

Vxe=integration(t,Axe);
Vxef=integration(t,Axef);
clf()
plot(t,Vxe)
plot(t,Vxef,"g")

Vxeff=Vxef-mmc(Vxef,200);
plot(t,Vxeff,"k")
plot(t,mmc(Vxef,200),"m")

Pxef=integration(t,Vxef);
Pxeff=integration(t,Vxeff);
clf()
plot(t,Pxef)
plot(t,Pxeff,"g")
