query = '''
SELECT [Lab_Code]
      ,[Lab_Name]
      ,[Process]
      ,[Previous_State]
      ,[Previous_Date]
      ,[Current_State]
      ,[Current_Date]
      ,[Internet_Connectivity]
      ,[Disa_Version]
  FROM [LabLogs].[dbo].[State]
  WHERE 
	CAST([Current_Date] AS DATE) = CAST(GETDATE()-1 AS DATE)
	AND (	
			[Previous_State] = 'Stopped' 
			OR [Current_State] = 'Stopped'
			OR [Internet_Connectivity] = 'Disconnected'
	);
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
  FROM [DisaLabsLogs].[dbo].[State]
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
  FROM [DisaLabsLogs].[dbo].[State]
  WHERE [Process] = {{}}
ORDER BY [Current_Date] DESC;
'''

total_labs = '''
SELECT COUNT(DISTINCT [Lab_Code]) AS Total_Checked_Labs
	  FROM [LabLogs].[dbo].[State]
  WHERE 
	CAST([Current_Date] AS DATE) = CAST(GETDATE()-1 AS DATE)
'''
