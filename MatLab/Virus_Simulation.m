clear all
% NOTE: While I understand this program and have made a fair amount of personal changes to it.
% I did not make this. It was made by a friend and his two classmates. To my knowledge they do not have a GitHub
% so I can't link to their profiles. However, I just wanted to say I don't take credit for more than understanding
% and some modifications.




tic
%Initial cell numbers, in billions per litre of blood:
%Viral particles
Vi = 200;
[V, V2, V3, V4] = deal(Vi);
%v = [];
I = 0.2; %Viral infection of T cells rate

%Target cells 
T = 5000;
%Rate of production of target cells per hour/per time period
Lamda = 0.0083;
%The death of healthy target cells as a percentage of their total
%population
Delta = 0.0083;
%The death of the immune system cells
DeltaA = 0.04;

%Setting the initial values for time, blood cell cout and immune system
%cells, attack (A) and memory (M) that have been exposed to the virus
Tp = [];
t = [];
A = 4; %attack
a = [];
M = 0; %memory
m = [];

%Messages
dead = 'EVERYBODY''S DEAD DAVE!';
alive = 'All good';

%Better coding practice (Part 1) - (See part 2 at end of FOR loop)
Tp = zeros(1500+1,1);
v = zeros(1500+1,1);
a = zeros(1500+1,1);
t = zeros(1500+1,1);
m = zeros(1500+1,1);
for ti = 0:1:1500 % Run experiment for 1,500 days, starting at 0 and incrementing by 1.
    
      %Indentical viral infections (Same volume) enter the bloodstream.
      %Each infection is spaced 250 days apart
      if (ti == 250) %When 250 days have passed 
          V = Vi;         
      elseif(ti == 500)
          V = V2; 
      elseif(ti == 750)
          V = V3;
      elseif(ti == 1000)
          V = V4;
      end
      
      Lamda = (41.5/(T)); %Making the growth rate of T (red blood) cells increase when the number of cells drops
      V = (V + I*V - (A*0.5)); %The number of virus pathogens = the origional number plus (the infection rate multiplied by the cells possible to infect (T cells))
      
      if (V < 0) %Making sure the virus doesn't go negative and mess up the system
          V = 0;
      end
      
      T = (T  + (Lamda*T) - (Delta*T) - (V*T*0.000012)); %Red blood cell count, using growth rate, death rate and the virus causes fatalities
      A = (A + (V*0.04) + (M*0.01) - (DeltaA*A)); %Attack anti-bodies, growth rate dependant on the amount of viral particles, the number of memory cells and a natural death rate
      M = (M + (V*0.005)); %Antibody memory cells, growth rate purely dependant on the number of viral cells, no natural death rate in this time span (growth rate = rate at which M cells are exposed to this virus)   
      floor(T); %There are no half particles so this rounds down to the below integer
           
      if  (T < 200)
          disp(dead)    
          dave = 1;
          break 
      elseif (V < 0)
          V = 0;
      else 
          dave = 0;      
      end 
      
      %Original (non-ideal) coding practice (consumes more resources)
      %Tp = [Tp T]
      %v = [v V];
      %a = [a A];
      %t = [t ti];
      %m = [m M];
      
      %Better coding practice (Part 2)
      Tp(ti+1) = T; %Tp = [Tp T]
      v(ti+1) = V;
      a(ti+1) = A;
      t(ti+1) = ti;
      m(ti+1) = M;
end

plot(t,Tp,t,v,t,a,t,m)
title('Viral infection in the human bloodstream');
legend('Red blood cells','Viral pathogens','Immune system attack cells','Immune system memory cells','LOCATION','East')
xlabel('Time, days')
ylabel('Cells, in billions')

if dave == 0
    disp(alive)
end
toc
