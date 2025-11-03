using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using UnityEngine;

public class UnityClient : MonoBehaviour
{
    private readonly HttpClient _http = new HttpClient();

    public async Task<string> Login(string playerId, string baseUrl = "http://localhost:8000")
    {
        var payload = new { player_id = playerId };
        var json = System.Text.Json.JsonSerializer.Serialize(payload);
        var resp = await _http.PostAsync($"{baseUrl}/api/login", new StringContent(json, Encoding.UTF8, "application/json"));
        resp.EnsureSuccessStatusCode();
        var body = await resp.Content.ReadAsStringAsync();
        // naive parse
        var token = System.Text.Json.JsonDocument.Parse(body).RootElement.GetProperty("token").GetString();
        return token;
    }
}
