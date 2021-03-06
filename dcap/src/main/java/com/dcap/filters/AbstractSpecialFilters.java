package com.dcap.filters;

import com.dcap.service.threads.FilterData;
import com.dcap.fileReader.DataFile;
import com.dcap.service.threads.FilterData;

import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/**
 * @author uli
 */
public abstract class AbstractSpecialFilters extends AbstractDataFilter {
    /**
     * Field to store the information, if there was chnanged the count of the columns
     */
    private Boolean columnCountChanged=false;



    /**
     * Construtctor for the AbstratctChangingFilter
     * @param name the name of the filter
     * @param columns map that contains the list of all strings that must be considerated, value is the name of the column in the experiment, the
     *                key is the name of the column in the csv file
     */
    public AbstractSpecialFilters(String name, Map<String, String> columns, Map<String, String> parameter) {
        super(name, columns, parameter);
    }

    /**
     * returns the description of the parameters that are needed as input. Returns the mame of the parameter as key and the type as value
     * @return list of required parameters
     */
    @Override
    public Map<String, ENUMERATED_TYPES> getRequiredParameters() {
        return null;
    }

    /**
     * Runs the filter.
     *
     *  @param data
     *            the data for the filtering
     * @return additional information generated by the filter to be displayed to the user.
     * @throws Exception
     *             if something goes wrong
     */
    @Override
    public List<FilterData> run(List<FilterData> data) throws Exception {
        return null;
    }

    /**
     * function that informs if the count of columns is changed
     * @return true if the count changed, false in the other case
     */
    public Boolean isColumnCountChanged(){
        return columnCountChanged;
    }

    /**
     * sets the field {@link #columnCountChanged}
     * @param flag value for the value
     */
    protected void setColumnsCountChanged(Boolean flag){
        this.columnCountChanged=flag;
    }
}
