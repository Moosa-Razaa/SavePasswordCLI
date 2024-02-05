using Application.Interfaces;

namespace Application.Actions;

public class Error : IActionHandler
{
    public void HandleAction()
    {
        Console.WriteLine("Error");
    }
}