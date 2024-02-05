using Application.Actions;
using Application.Interfaces;

namespace Application;

public class HandleInitialInput
{
    private readonly string _userInput;
    private const string Create = "create";
    private const string Read = "read";
    private const string Update = "update";
    private const string Delete = "delete";
    
    public HandleInitialInput(string userInput)
    {
        _userInput = userInput;
    }

    public IActionHandler ParseInput()
    {
        string[] input = _userInput.Split(' ');
        if (input.Length > 2) return new Error();
        
        

        return input[0] switch
        {
            Create => new Create(""),
            Read => new Read(""),
            Update => new Update(""),
            Delete => new Delete(""),
            _ => new Error()
        };
    }
}