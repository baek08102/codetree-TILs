using System;

public class Codetree
{  
    public static void Main()
    {
        string input = Console.ReadLine();

        string[] numbers = input.Split(' ');

        int a = int.Parse(numbers[0]);
        int b = int.Parse(numbers[1]);
        
        Console.Write($"{a/b}...{a%b}");
    }
}
