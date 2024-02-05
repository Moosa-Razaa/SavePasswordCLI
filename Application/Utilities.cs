using System.Text;

namespace Application;

public static class Utilities
{
    public static string ReadConfidentialInput()
    {
        string password = string.Empty;

        ConsoleKey currentKeyPressed;
        do
        {
            ConsoleKeyInfo keyInfo = Console.ReadKey(intercept: true);
            currentKeyPressed = keyInfo.Key;

            if (currentKeyPressed == ConsoleKey.Backspace && password.Length > 0)
            {
                Console.Write("\b \b");
                password = password[..^1];
            }
            else if (!char.IsControl(keyInfo.KeyChar))
            {
                Console.Write("*");
                password += keyInfo.KeyChar;
            }
        } while (currentKeyPressed != ConsoleKey.Enter);
        
        return password;
    }
}