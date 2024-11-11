import logging
import pandas as pd
from pathlib import Path
from .serializer import EmployeeSerializer, DepartmenSerializer, JobSerializer

logger = logging.getLogger('file_utils')

def process_request(lstFile_Names: list, strEnum: str):
    if strEnum == 'EMPLOYEE':
        lstdictEmployees = extract_employee_file(lstFile_Names)

        return EmployeeSerializer(data=lstdictEmployees, many=True)
    elif strEnum == 'DEPARTMENT':
        lstdictDepartment = extract_departments_file(lstFile_Names)

        return DepartmenSerializer(data=lstdictDepartment, many=True)
    elif strEnum == 'JOB':
        lstdicJob = extract_jobs_file(lstFile_Names)

        return JobSerializer(data=lstdicJob, many=True)

def validate_paths(lstFile_Names: list) -> list:

    if  len(lstFile_Names) < 1:
        raise IndexError('At least one element is excpected')
    else:
        setPaths_Error = set()

        for strFile_Name in lstFile_Names:
            pathFile_Path = Path(strFile_Name)

            if not pathFile_Path.exists():
                logger.error(strFile_Name + " file path provided does not exist")
                setPaths_Error.add(strFile_Name) 

        lstFiltered_File_Names = [strFile_Name for strFile_Name in lstFile_Names if strFile_Name not in setPaths_Error]

        if len(lstFiltered_File_Names) < 1:
            raise IndexError('No viable file path provided')
        
        return lstFiltered_File_Names
    
def extract_employee_file(lstFile_Names: list) -> list:
    
    try:
        lstFiltered_File_Names = validate_paths(lstFile_Names)

        lstEmployee_DFs = []
        lstHeader_Names = ['id', 'name', 'datetime', 'department_id', 'job_id']
        
        for strFile_Name in lstFiltered_File_Names:
            try:
                
                dfAux = pd.read_csv(strFile_Name,names= lstHeader_Names, parse_dates=['datetime'])
                dfAux['job_id'] = dfAux['job_id'].astype('Int64')
                dfAux['department_id'] = dfAux['department_id'].astype('Int64')

                lstReport_Datetime = dfAux[dfAux['datetime'].isna()]['id'].to_list()
                logger.warning('In File ' + strFile_Name + ' the following Employees ids do not have Datetimefield: ' + str(lstReport_Datetime))

                lstReport_Job_ID = dfAux[dfAux['job_id'].isna()]['id'].to_list()
                logger.warning('In File ' + strFile_Name + ' the following Employees ids do not have Job ID: ' + str(lstReport_Job_ID))

                lstReport_Department_ID = dfAux[dfAux['department_id'].isna()]['id'].to_list()
                logger.warning('In File ' + strFile_Name + ' the following Employees ids do not have Department ID: ' + str(lstReport_Department_ID))

                dfAux = dfAux[(dfAux['datetime'].notna()) & (dfAux['job_id'].notna()) & (dfAux['department_id'].notna())]

                lstEmployee_DFs.append(dfAux)
            except KeyError:
                logging.error(strFile_Name + " a value in the file can not be converted")

        dfAux = pd.concat(lstEmployee_DFs)
        lstdictEmployees = dfAux.to_dict('records')

        for dictEmployee in lstdictEmployees:
            dictEmployee['datetime'] = dictEmployee['datetime'].to_pydatetime()

        return lstdictEmployees
    except IndexError:
        pass

def extract_departments_file(lstFile_Names: list) -> list:
    
    try:
        lstFiltered_File_Names = validate_paths(lstFile_Names)

        lstDepartments_DFs = []
        lstHeader_Names = ['id', 'department']
        
        for strFile_Name in lstFiltered_File_Names:
            try:
                
                dfAux = pd.read_csv(strFile_Name,names= lstHeader_Names)

                lstReport_Datetime = dfAux[dfAux['department'].isna()]['id'].to_list()
                logger.warning('In File ' + strFile_Name + ' the following Employees ids do not have Department: ' + str(lstReport_Datetime))

                dfAux = dfAux[dfAux['department'].notna()]

                lstDepartments_DFs.append(dfAux)
            except KeyError:
                logging.error(strFile_Name + " a value in the file can not be converted")

        dfAux = pd.concat(lstDepartments_DFs)
        return dfAux.to_dict('records')

    except IndexError:
        pass

def extract_jobs_file(lstFile_Names: list) -> list:
    
    try:
        lstFiltered_File_Names = validate_paths(lstFile_Names)

        lstJobs_DFs = []
        lstHeader_Names = ['id', 'job']
        
        for strFile_Name in lstFiltered_File_Names:
            try:
                
                dfAux = pd.read_csv(strFile_Name,names= lstHeader_Names)

                lstReport_Datetime = dfAux[dfAux['job'].isna()]['id'].to_list()
                logger.warning('In File ' + strFile_Name + ' the following Employees ids do not have Job: ' + str(lstReport_Datetime))

                dfAux = dfAux[dfAux['job'].notna()]

                lstJobs_DFs.append(dfAux)
            except KeyError:
                logging.error(strFile_Name + " a value in the file can not be converted")

        dfAux = pd.concat(lstJobs_DFs)
        return dfAux.to_dict('records')

    except IndexError:
        pass