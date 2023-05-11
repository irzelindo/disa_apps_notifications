query = '''
SELECT [Lab_Code] 
	  ,[Lab_Name]
      ,[Process]
      ,[Previous_State]
      ,CAST([Previous_Date] AS VARCHAR)
      ,[Current_State]
      ,CAST([Current_Date] AS VARCHAR)
      ,[Internet_Connectivity]
  FROM [LabLogs].[dbo].[State]
  WHERE CAST([Current_Date] AS DATE) = CAST(GETDATE()-1 AS DATE)
ORDER BY [Current_Date] DESC;
'''

query_date_params = f'''
SELECT [Lab_Code] 
	  ,[Lab_Name]
      ,[Process]
      ,[Previous_State]
      ,[Previous_Date]
      ,[Current_State]
      ,[Current_Date]
      ,[Internet_Connectivity]
  FROM [LabLogs].[dbo].[State]
  WHERE CAST([Current_Date] AS DATE) BETWEEN {{}} AND {{}}
ORDER BY [Current_Date] DESC;
'''

query_process_params = f'''
SELECT [Lab_Code] 
	  ,[Lab_Name]
      ,[Process]
      ,[Previous_State]
      ,[Previous_Date]
      ,[Current_State]
      ,[Current_Date]
      ,[Internet_Connectivity]
  FROM [LabLogs].[dbo].[State]
  WHERE [Process] = {{}}
ORDER BY [Current_Date] DESC;
'''
