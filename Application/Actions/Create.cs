using Application.Interfaces;

namespace Application.Actions;

public class Create : IActionHandler
{
    private readonly string _domain;
    
    public Create(string domain)
    {
        _domain = domain;
    }
    
    public void HandleAction()
    {
        
    }
}