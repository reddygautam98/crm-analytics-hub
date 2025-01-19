-- Basic client count
SELECT COUNT(*) as total_clients
FROM clients;

-- Email domain distribution
SELECT 
    SUBSTRING_INDEX(Email_Phone, '@', -1) as domain,
    COUNT(*) as count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM clients), 2) as percentage
FROM clients
WHERE Email_Phone LIKE '%@%'
GROUP BY domain
ORDER BY count DESC;

-- Client name word analysis
SELECT 
    CASE 
        WHEN Client_Name LIKE '% Ltd%' THEN 'Ltd'
        WHEN Client_Name LIKE '% Inc%' THEN 'Inc'
        WHEN Client_Name LIKE '% PLC%' THEN 'PLC'
        WHEN Client_Name LIKE '% LLC%' THEN 'LLC'
        WHEN Client_Name LIKE '% Group%' THEN 'Group'
        ELSE 'Other'
    END as company_type,
    COUNT(*) as count
FROM clients
GROUP BY company_type
ORDER BY count DESC;

-- Contact person title analysis
SELECT 
    CASE 
        WHEN Contact_Person LIKE '% PhD%' THEN 'PhD'
        WHEN Contact_Person LIKE '% MD%' THEN 'MD'
        WHEN Contact_Person LIKE '% DVM%' THEN 'DVM'
        ELSE 'No Title'
    END as title,
    COUNT(*) as count
FROM clients
GROUP BY title
ORDER BY count DESC;

Results in CSV format:

Analysis Type,Category,Count,Percentage
Total Clients,All,50,100%
Email Domain Distribution,gmail.com,13,26%
Email Domain Distribution,yahoo.com,12,24%
Email Domain Distribution,hotmail.com,10,20%
Email Domain Distribution,Other Domains,15,30%
Company Type,Ltd,12,24%
Company Type,Inc,8,16%
Company Type,Group,5,10%
Company Type,PLC,3,6%
Company Type,LLC,2,4%
Company Type,Other,20,40%
Professional Titles,No Title,47,94%
Professional Titles,PhD,1,2%
Professional Titles,MD,1,2%
Professional Titles,DVM,1,2%
