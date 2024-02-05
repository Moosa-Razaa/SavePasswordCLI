using Application.Interfaces;

namespace Application.Actions;

public class Delete : IActionHandler
{
    private readonly string _domain;

    public Delete(string domain)
    {
        _domain = domain;
    }
    
    public void HandleAction()
    {
        
    }
}