using System;

namespace TVACalc
{
    internal class Program
    {
        static void Main(string[] args)
        {
            const double TN = 0.2;
            const double TI = 0.1;
            const double TR = 0.055;
            const double TP = 0.021;

            Console.WriteLine("Bonjour, bienvenue dans ce programme");
            Console.WriteLine("Voici les taux de TVA en vigueur en France : " + "\n" +
                               "Taux normal : " + TN + "\n" + "Taux intermédiaire : " + TI + "\n" +
                               "Taux réduit : " + TR + "\n" + "Taux particulier : " + TP);
            Console.Write("Veuillez taper TN pour le taux normal, TI pour le taux intermédiaire, TR pour le taux réduit et TP pour le taux particulier : ");
            string TAUX_CHOISI;
            TAUX_CHOISI = Console.ReadLine();
            if (TAUX_CHOISI != "TN" && TAUX_CHOISI != "TI" && TAUX_CHOISI != "TR" && TAUX_CHOISI != "TP")
            {
                Console.Write("Veuiller saisir une valeur dans la liste suivante : TN, TI, TR, TP");
                Console.Read();
                return;
            }
            Console.Write("Entrer le montant : ");
            double MONTANT = double.Parse(Console.ReadLine());

            double RESULTAT = 0;
            if (TAUX_CHOISI == "TN")
            {
                RESULTAT = MONTANT * TN;
            }
            else if (TAUX_CHOISI == "TI")
            {
                RESULTAT = MONTANT * TI;
            }
            else if (TAUX_CHOISI == "TR")
            {
                RESULTAT = MONTANT * TR;
            }
            else if (TAUX_CHOISI == "TP")
            {
                RESULTAT = MONTANT * TP;
            }

            Console.WriteLine("La TVA pour le montant saisi est de " + RESULTAT + " EUR");
            Console.ReadLine();
        }
    }
}
