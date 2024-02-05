using Application.Interfaces;

namespace Application.Actions;

public class Read : IActionHandler
{
    private readonly string _domain;

    public Read(string domain)
    {
        _domain = domain;
    }

    public void HandleAction()
    {
        
    }

}