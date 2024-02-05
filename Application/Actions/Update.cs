using Application.Interfaces;

namespace Application.Actions;

public class Update : IActionHandler
{
    private readonly string _domain;

    public Update(string domain)
    {
        _domain = domain;
    }
    
    public void HandleAction()
    {
        
    }
}