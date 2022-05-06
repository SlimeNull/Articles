---
title: "[C#] EleCho.Json: 便捷, 简单以及高速的 JSON 操作"
date: 2022-03-26T22:21:12+08:00
tags:
  - .NET
  - C#
  - 算法
  - 轮子
---

便捷, 简单以及高速的 JSON 读写器. 同时以也可以使用实体类来操作 JSON 数据.

<!--more-->

EleCho.Json 是我目前最新开发的开源 JSON 解析库, 它的代码是目前的我所能写出来最优的, 相比之前写过的 CHO.Json, EleCho.Json 是更加简单的, 并且更加灵活. 主要是追求较高速率, 不要求复杂特性的简易 JSON 操作, 例如最基本类型的转换.

开源仓库: [SlimeNull/EleCho.Json](https://github.com/SlimeNull/EleCho.Json), 欢迎提交 Pull Request.

速度约为 Newtonsoft.Json 的 1.89 倍, System.Text.Json 的 7.92 倍, 你也可以在 TestConsole 项目中自己运行该测试

## 安装 EleCho.Json

你可以通过 NuGet 安装 EleCho.Json.
`NuGet: Install-Package EleCho.Json`

或者在 Visual Studio 中, 使用 Nuget 包管理器安装 EleCho.Json.

## JSON 对象

EleCho.Json 中, 所有的 JSON 数据, 包括数组, 字典, 字符串, 数字, 布尔值, null, 都能够直接去存储与操作值.

例如 JsonObject 是 JSON 对象, 用于存储键值对, 在 EleCho.Json, 它直接继承于 Dictionary&lt;string, object&gt;, 它的值可以是任意类型的. 包括 JsonArray 也是继承于 List&lt;object&gt;.

```csharp
JsonObject jObj = new JsonObject();    // JSON 对象 (键值对存储)
jObj.Add("some_key", "any_value");     // 使用字符串键设置值
jObj["some_key"] = new JsonString("Some string value");   // 或者使用 "this[...]" 和 IJsonData 设置

JsonArray jArr = new JsonArray();      // JSON 数组 (列表存储)
jArr.Add("Any value");                 // 添加任何 JSON 数据
jArr.Add(new JsonString("Anything"));  // 或者使用 JsonString

JsonString jStr = "QWQ";               // 使用隐式类型转换创建 JSON 字符串
JsonNumber jNum = 114514;              // 床架 JSON 数字 (它使用 double 存储)
JsonBoolean jBl = true;                // 创建 JSON 逻辑值(布尔值)
JsonNull = new JsonNull();             // JSON null, 或者使用 JsonData.Null

// Read JSON data:
string someStr = jObj["some_key"] as JsonString;   // 从 JSON 对象中读取 JSON 字符串
int someNum = jObj["some_key_num"] as JsonNumber;  // 从 JSON 对象中读取 JSON 数字
```

## 通过流操作 JSON 数据

EleCho.Json 提供了 JsonWriter 和 JsonReader 来实现 JSON 数据的写入和读取. 构造函数接受一个 Stream 或 TextWriter/TextReader.

将 JSON 数据写入到流
```csharp
Stream stream;  // 要写入的 Stream
IJsonData someJsonData;
JsonWriter jw = new JsonWriter(stream);
jw.Write(someJsonData);
```

从流中读取 IJsonData:
```csharp
Stream stream;  // 要读取的 Stream
JsonReader jr = new JsonReader(stream);   // 实例化 JSON 读取器
IJsonData jsonData = jr.Read();           // 从流中读取一个完整的 JSON 数据
```

## 值与 JSON 数据的转换

从任意创建 JSON 数据
```csharp
IJsonData jsonData = JsonData.FromValue(new()
{
    Name = "SlimeNull",
    Age = 18,
    Description = "CSharper! love .NET (*/ω＼*)"
});
```

从 JSON 数据创建模型对象
```csharp
class One
{
    public string Name;
    public int Age;
    public string Description;
    
    // 在这里你也可以使用属性
}

void LogicalCode()
{
    JsonObject someJsonData;   // 要处理的 JSON 数据
    One model = JsonData.ToValue(typeof(One), someJsonData);
}
```

## 序列化与反序列化

将对象序列化为 JSON 字符串
```csharp
class One
{
    public string Name;
    public int Age;
    public string Description;
}

void LogicalCode()
{
    One model = new One() { Name = "SlimeNull", Age = 18, Description = "Some text" };
    string jsonText = JsonSerializer.Serialize(model);
}
```

从 JSON 字符串反序列化
```csharp
class One
{
    public string Name;
    public int Age;
    public string Description;
}

void LogicalCode()
{
    string jsonTxt;
    One model = JsonSerializer.Deserialize<One>(jsonTxt);
}
```

## 从流中读取 JsonToken

从流中解析 JSON token
```csharp
Stream stream;     // 要读取的流
JsonParser jParser = new JsonParser(stream);
jParser.PeekToken();   // 从流中读取一个 token, 但不变更当前的读取状态
jParser.ReadToken();   // 从流中读取一个 token, 并移动到下一个 token
```